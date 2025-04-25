import psycopg2
from config import load_config

def create_phonebook_table():
    command = """
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                print("PhoneBook table created successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)

if __name__ == '__main__':
    create_phonebook_table()
