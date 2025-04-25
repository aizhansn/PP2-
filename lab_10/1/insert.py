import csv
import psycopg2
from connect import connect
from config import load_config

def insert_from_csv(filename):
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            name, phone = row
            cur.execute("""
                INSERT INTO phonebook (name, phone)
                VALUES ( %s, %s)
            """, (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    config = load_config()
    conn = connect(config)
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO phonebook (name, phone)
            VALUES (%s, %s)
        """, (name, phone))
        conn.commit()
    except psycopg2.errors.UniqueViolation:
        print("Error: Phone number must be unique.")
        conn.rollback()

    cur.close()
    conn.close()

insert_from_csv("contacts.csv")
insert_from_console()
