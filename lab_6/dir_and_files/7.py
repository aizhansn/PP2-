import shutil

source = input()
destination = input()

try:
    shutil.copy(source, destination)
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
