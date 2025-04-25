import psycopg2
from connect import connect, load_config

def query_data():
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    print("Query by:")
    print("1. Name")
    print("2. Phone")
    print("3. All records")
    choice = input("Enter the number: ")

    if choice == '1':
        name = input("Enter the name: ")
        cur.execute("""
            SELECT * FROM phonebook
            WHERE name ILIKE %s
        """, ('%' + name + '%',)) #IlIKE case sensitive
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found.")

    elif choice == '2':
        phone = input("Enter the phone: ")
        cur.execute("""
            SELECT * FROM phonebook
            WHERE phone = %s
        """, (phone,))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found.")

    elif choice == '3':
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found.")

    else:
        print("Invalid choice.")

    cur.close()
    conn.close()

query_data()