import re
from pathlib import Path

file_path = Path("c:/Study/pp2/lab_5/raw.txt")
with file_path.open("r", encoding="utf-8") as file:
    receipt_data = file.read()

replaced_chars = re.sub(r'[ ,.]', ':', receipt_data)

print(replaced_chars[:200])
