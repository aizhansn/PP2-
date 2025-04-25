import psycopg2
from connect import connect, load_config

def delete_data():
    config = load_config()  # Load configuration
    conn = connect(config)  # Connect to the database
    cur = conn.cursor()

    print("Delete by:")
    print("1. Name")
    print("2. Phone")
    choice = input("Enter the number: ")

    if choice == '1':
        name = input("Enter the name: ")
        cur.execute("""
            DELETE FROM phonebook
            WHERE name = %s
        """, (name,))
        if cur.rowcount > 0:
            print(f"User {name} deleted successfully.")
        else:
            print("No user found")

    elif choice == '2':
        phone = input("Enter the phone number: ")
        cur.execute("""
            DELETE FROM phonebook
            WHERE phone = %s
        """, (phone,))
        if cur.rowcount > 0:
            print(f"User with phone {phone} deleted successfully.")
        else:
            print("No user found")

    else:
        print("Invalid choice.")

    conn.commit()
    cur.close()
    conn.close()

delete_data()