import sys
import os

print("Current working directory:", os.getcwd())
print("Python path:")
for path in sys.path:
    print(f"  - {path}")

print("\nTrying to import app.main:")
try:
    import app.main
    print("Success! app.main imported from:", app.main.__file__)
except ImportError as e:
    print(f"Error importing app.main: {e}")
