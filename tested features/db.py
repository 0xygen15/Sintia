import sqlite3

connection = sqlite3.connect("./database/users.db")
c = connection.cursor()

c.execute("select user_id from users")
data = c.fetchall()
for item in data:
    print(item)

connection.close()



