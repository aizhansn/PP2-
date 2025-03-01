import os

def check_path_access(path):
    if os.path.exists(path):
        print(f"Path: {path} exists")
        print(f"Readable: {'Yes' if os.access(path, os.R_OK) else 'No'}")
        print(f"Writable: {'Yes' if os.access(path, os.W_OK) else 'No'}")
        print(f"Executable: {'Yes' if os.access(path, os.X_OK) else 'No'}")
    else:
        print(f"Path: {path} does not exist")

path_to_check = "c:/Study/pp2/lab_5/raw.txt"
check_path_access(path_to_check)
