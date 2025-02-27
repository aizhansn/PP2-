file_path = "output.txt"
data = ["Hello", "Python", "File Handling"]

with open(file_path, "w", encoding="utf-8") as file:
    for item in data:
        file.write(item + "\n")

print("List written to file:", file_path)
