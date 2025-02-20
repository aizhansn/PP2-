import re
from pathlib import Path

file_path = Path("c:/Study/pp2/lab_5/raw.txt")
with file_path.open("r", encoding="utf-8") as file:
    receipt_data = file.read()

split_at_uppercase = re.findall(r'[A-Z][^A-Z]*', receipt_data)

print(split_at_uppercase[:10])
