# import sqlite3
#
# # filename to form database
# file = "users.db"
#
# try:
#     conn = sqlite3.connect(file)
#     print("Database Sqlite3.db formed.")
# except:
#     print("Database Sqlite3.db not formed.")

import psycopg2

try:
    # connect to exist database
    connection = psycopg2.connect(
        host="172.19.0.2",
        user="sintia",
        password="example",
        database="users",
        port="5432"
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
