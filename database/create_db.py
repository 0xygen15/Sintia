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
    print('entered')
    connection = psycopg2.connect(
        host="127.0.0.2",
        user="sintia",
        password="example",
        database="users",
        port="5432"
    )
    # connection.autocommit = True
    print('connected')
    # Create a cursor object using the connection
    cursor = connection.cursor()
    print('cursor created')
    # Execute a test query to check the connection
    cursor.execute("SELECT version();")
    print('select executed')
    # Fetch the result
    db_version = cursor.fetchone()
    print('fetched')
    print("Successfully connected to PostgreSQL")
    print("PostgreSQL version:", db_version)

    # Close the cursor and connection
    cursor.close()
    connection.close()


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
