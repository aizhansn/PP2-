import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt")
        
print("26 text files created.")
