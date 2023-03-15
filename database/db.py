import sqlite3

connection = sqlite3.connect("db.db")
c = connection.cursor()

c.execute("select * from truth where level='adult'")
data = c.fetchall()
for item in data:
    print(item)

connection.close()



