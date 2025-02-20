import re
from pathlib import Path

file_path = Path("c:/Study/pp2/lab_5/raw.txt")
with file_path.open("r", encoding="utf-8") as file:
    receipt_data = file.read()

lowercase_with_underscore = re.findall(r'\b[a-z]+_[a-z]+\b', receipt_data)

print(lowercase_with_underscore)
