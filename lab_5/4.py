import re
from pathlib import Path

file_path = Path("c:/Study/pp2/lab_5/raw.txt")
with file_path.open("r", encoding="utf-8") as file:
    receipt_data = file.read()

uppercase_followed_by_lowercase = re.findall(r'\b[A-Z][a-z]+\b', receipt_data)

print(uppercase_followed_by_lowercase)
