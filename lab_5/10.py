import re
from pathlib import Path

file_path = Path("c:/Study/pp2/lab_5/raw.txt")
with file_path.open("r", encoding="utf-8") as file:
    receipt_data = file.read()

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

camel_case_strings = re.findall(r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)*\b', receipt_data)
snake_case_converted = [camel_to_snake(s) for s in camel_case_strings]

print(snake_case_converted)
