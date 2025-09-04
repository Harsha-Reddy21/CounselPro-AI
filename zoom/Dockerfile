FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose port for FastAPI
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "zoom_integration:app", "--host", "0.0.0.0", "--port", "8000"]
