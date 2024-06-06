import sqlite3

def insert_transaction(date, amount):
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    print(date, amount)
    cursor.execute('''
    INSERT INTO transactions (date, amount)
    VALUES (?, ?)
    ''', (date, amount))
    conn.commit()
    conn.close()

def get_all_transactions():
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    rows = cursor.fetchall()
    conn.close()
    return rows
