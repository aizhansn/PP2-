from connect import connect
from config import load_config

def search_by_pattern():
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    pattern = input("Enter pattern: ")

    cur.execute("""
        SELECT * FROM phonebook WHERE name LIKE %s OR phone LIKE %s;
    """, ('%' + pattern + '%', '%' + pattern + '%'))
    results = cur.fetchall()
    if results:
        print("Results:")
        for name, phone in results:
            print(f"{name}: {phone}")
    else:
        print("No results found for the given pattern")

    cur.close()
    conn.close()


def insert_or_update_user():
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    existing_user = cur.fetchone()

    if existing_user:
        cur.execute("""
            UPDATE phonebook
            SET phone = %s
            WHERE name = %s
        """, (phone, name))
        print(f"Phone number for {name} updated successfully")
    else:
        cur.execute("""
            INSERT INTO phonebook (name, phone)
            VALUES (%s, %s)
        """, (name, phone))
        print(f"User {name} added successfully")

    conn.commit()
    cur.close()
    conn.close()


def insert_many_users():
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    invalid_data = []

    while True:
        name = input("Enter name (or 'stop'): ")
        if name.lower() == 'stop':
            break

        phone = input("Enter phone: ")

        if phone.isdigit() and len(phone) >= 5:
            cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
            existing_user = cur.fetchone()

            if existing_user:
                cur.execute("""
                    UPDATE phonebook
                    SET phone = %s
                    WHERE name = %s
                """, (phone, name))
                print(f"Phone number for {name} updated successfully")
            else:
                cur.execute("""
                    INSERT INTO phonebook (name, phone)
                    VALUES (%s, %s)
                """, (name, phone))
                print(f"User {name} added successfully")
        else:
            invalid_data.append((name, phone))
            print("Invalid phone")

    conn.commit()

    if invalid_data:
        print("\nInvalid entries:")
        for name, phone in invalid_data:
            print(f"- {name}: {phone}")
    else:
        print("\nAll users inserted/updated successfully.")

    cur.close()
    conn.close()


def get_users_by_page():
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    limit = input("Enter limit: ")
    offset = input("Enter offset: ")

    cur.execute("""
        SELECT * FROM phonebook LIMIT %s OFFSET %s;
    """, (limit, offset))

    results = cur.fetchall()
    if results:
        print("Results:")
        for row in results:
            print(row)
    else:
        print("No results found")

    cur.close()
    conn.close()


def delete_data():
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    print("Delete by:")
    print("1. Name")
    print("2. Phone")
    choice = input("Enter the number: ")

    if choice == '1':
        name = input("Enter the name: ")
        cur.execute("""
            DELETE FROM phonebook
            WHERE name = %s;
        """, (name,))
        if cur.rowcount > 0:
            print(f"User {name} deleted successfully")
        else:
            print("No user found.")

    elif choice == '2':
        phone = input("Enter the phone number: ")
        cur.execute("""
            DELETE FROM phonebook
            WHERE phone = %s;
        """, (phone,))
        if cur.rowcount > 0:
            print(f"User with phone {phone} deleted successfully")
        else:
            print("No user found")

    else:
        print("Invalid choice")

    conn.commit()
    cur.close()
    conn.close()


def main():
    while True:
        print("\nPhoneBook Menu")
        print("1. Search by pattern")
        print("2. Insert or update")
        print("3. Insert many users")
        print("4. Get users with pagination")
        print("5. Delete user by name or phone")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            search_by_pattern()
        elif choice == '2':
            insert_or_update_user()
        elif choice == '3':
            insert_many_users()
        elif choice == '4':
            get_users_by_page()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            break
        else:
            print("Invalid option")


if __name__ == '__main__':
    main()
