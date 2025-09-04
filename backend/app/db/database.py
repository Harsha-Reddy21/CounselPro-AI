from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
import ssl

# Load .env file
load_dotenv()
# Get the database URL from environment variables
DATABASE_URL = os.getenv("ASYNC_DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("ASYNC_DATABASE_URL environment variable is not set.")

# Create async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,  # Shows SQL queries in console
)

# Create session maker
AsyncSession = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Base class for database models
Base = declarative_base()


# Database dependency
async def get_async_db():
    async with AsyncSession() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()


# Create database tables
async def create_tables():
    # Import all models to ensure they're registered
    from app.models.counselor import Counselor  # type: ignore
    from app.models.session import CounselingSession  # type: ignore
    from app.models.catalog_file import CatalogFile  # type: ignore

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# for celery
# =============================================================================================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SYNC_DATABASE_URL = os.getenv("DATABASE_URL") or DATABASE_URL.replace("asyncpg", "psycopg2")  # Use DATABASE_URL if available
sync_engine = create_engine(
    SYNC_DATABASE_URL,
    echo=True,
    future=True,
)
SyncSessionLocal = sessionmaker(
    bind=sync_engine,
    autocommit=False,
    autoflush=False,
)


# Dependency for sync Celery tasks
def get_sync_db():
    db = SyncSessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


# =============================================================================================


# Optional test function
if __name__ == "__main__":
    import asyncio
    from sqlalchemy import text

    async def test():
        async with engine.begin() as conn:
            result = await conn.execute(text("SELECT version();"))
            print(result.all())

    asyncio.run(test())
