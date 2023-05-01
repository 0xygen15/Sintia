import sqlite3

connection = sqlite3.connect("users.db")
c = connection.cursor()

query = "SELECT * FROM users"
c.execute(query)
rows = c.fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()