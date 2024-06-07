import sqlite3
from datetime import datetime


transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with sqlite3.connect("transactions.db") as db:
    cur = db.cursor()
    db.commit()
    cur.execute(
        """INSERT INTO transactions (date, amount)
                VALUES (?, ?)
             """,
        (transaction_date,100.0))

