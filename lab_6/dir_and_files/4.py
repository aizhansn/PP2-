def count_lines(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            print(f"Total lines in {file_path}: {len(lines)}")
    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print(f"Error: {e}")

file_path = "c:/Study/pp2/lab_5/raw.txt"
count_lines(file_path)
