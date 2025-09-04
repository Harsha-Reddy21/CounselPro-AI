import sys
import os

# Remove the conflicting path
for path in list(sys.path):
    if "full-stack-fastapi-template" in path:
        sys.path.remove(path)
        print(f"Removed path: {path}")

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
    print(f"Added path: {current_dir}")

# Print the updated path
print("Updated Python path:")
for path in sys.path:
    print(f"  - {path}")

# Run the app
import uvicorn

if __name__ == "__main__":
    print("Starting the server...")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
