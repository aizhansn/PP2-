import os

path = input()

if os.path.exists(path):
    print("\nDirectories:")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

    print("\nFiles:")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    print("\nAll contents:")
    print(os.listdir(path))
else:
    print("Path does not exist.")
