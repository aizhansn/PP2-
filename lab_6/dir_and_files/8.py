import os

file_path = input()

if os.path.exists(file_path) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File does not exist or cannot be deleted.")
