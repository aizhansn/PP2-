import psycopg2
from connect import connect, load_config

def update_data():
    config = load_config()
    conn = connect(config)

    cur = conn.cursor()

    choice = input("What do you want to update? (1 - name, 2 - phone): ")

    if choice == '1':
        phone = input("Enter the phone number to find the user: ")
        new_name = input("Enter the new name: ")

        cur.execute("""
            UPDATE phonebook
            SET name = %s
            WHERE phone = %s
        """, (new_name, phone))
        print("Name updated successfully.")

    elif choice == '2':
        name = input("Enter the name to find the user: ")
        new_phone = input("Enter the new phone number: ")

        cur.execute("""
            UPDATE phonebook
            SET phone = %s
            WHERE name = %s
        """, (new_phone, name))
        print("Phone number updated successfully.")

    else:
        print("Invalid choice.")

    conn.commit()
    cur.close()
    conn.close()

update_data()
