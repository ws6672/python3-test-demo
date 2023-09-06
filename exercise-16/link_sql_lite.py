import sqlite3
from sqlite3 import Connection

DEFAULT_NAME = '{}.db'

def open_or_create(db_name:str)->Connection:
    return sqlite3.connect(DEFAULT_NAME.format(db_name))

def init_data(conn:Connection):
    cursor =  conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS test_data (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    if count(conn)==0:
        cursor.execute("INSERT INTO test_data (name, age) VALUES (?, ?)", ('Alice', 25))
        cursor.execute("INSERT INTO test_data (name, age) VALUES (?, ?)", ('Bob', 30))
        conn.commit()
    cursor.close()

def count(conn:Connection)->int:
    cursor =  conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM test_data")
    row_number= cursor.fetchone()
    cursor.close()
    return row_number

def search(conn:Connection):
    cursor =  conn.cursor()
    cursor.execute("SELECT * FROM test_data")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

if __name__ == '__main__':
    with open_or_create('test') as conn:
        init_data(conn)
        search(conn)