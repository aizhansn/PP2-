import os

def check_path(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("Path does not exist")

path_to_test = "c:/Study/pp2/lab_5/raw.txt"
check_path(path_to_test)
