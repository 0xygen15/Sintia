#
#
#
# # connect to exist database
# # print('entered')
# # connection = psycopg2.connect(
# #     host="127.0.0.3",
# #     user="sintia",
# #     password="example",
# #     database="users",
# #     port="5432"
# # )
# #
# # cursor = connection.cursor()
# # cursor.execute("SELECT version();")
# # db_version = cursor.fetchone()
# #
# # print("Successfully connected to PostgreSQL")
# # print("PostgreSQL version:", db_version)
# # cursor.close()
# # connection.close()
#
# # except Exception as _ex:
# #     print("[INFO] Error while working with PostgreSQL", _ex)
#
# import sqlite3
# import psycopg2
# import pickle
#
# from mainUnit.config import DB_HOST, DB_PORT, DB_USERNAME, DB_PWD
#
# from mainUnit.users import Users, user_objects
#
# class Database:
#     @classmethod
#     def create_users_db(cls):
#         connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database="users",port=DB_PORT)
#         cursor = connection.cursor()
#
#         query = """
#             CREATE TABLE IF NOT EXISTS users (
#             user_id CHAR UNIQUE,
#             lang_code CHAR,
#             tord_game BLOB,
#             nie_game BLOB,
#             the_35_game BLOB,
#             themes_game BLOB,
#             tord_kb BLOB,
#             nie_kb BLOB,
#             the_35_kb BLOB,
#             themes_kb BLOB,
#             chat_id CHAR,
#             chat_type CHAR,
#             username CHAR,
#             fName CHAR,
#             lName CHAR,
#             is_bot INTEGER
#             )
#             """
#
#         cursor.execute(query)
#
#         connection.commit()
#         connection.close()
#
#     @classmethod
#     def add_user_to_db(cls, users_obj: Users):
#         user_id = users_obj.user_id
#         lang_code = users_obj.lang_code
#
#         tord_game = pickle.dumps(users_obj.tord_game)
#         nie_game = pickle.dumps(users_obj.nie_game)
#         the_35_game = pickle.dumps(users_obj.the_35_game)
#         themes_game = pickle.dumps(users_obj.themes_game)
#
#         tord_kb = pickle.dumps(users_obj.tord_kb)
#         nie_kb = pickle.dumps(users_obj.nie_kb)
#         the_35_kb = pickle.dumps(users_obj.the_35_kb)
#         themes_kb = pickle.dumps(users_obj.themes_kb)
#
#         chat_id = users_obj.chat_id
#         chat_type = users_obj.chat_type
#         username = users_obj.username
#         fName = users_obj.fName
#         lName = users_obj.lName
#         is_bot = int(users_obj.is_bot)
#
#         connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database="users", port=DB_PORT)
#         cursor = connection.cursor()
#
#         try:
#             cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
#             result = cursor.fetchone()[0]
#         except:
#
#             # if result is None:
#             query = """
#                         INSERT INTO users (user_id, lang_code, tord_game, nie_game,
#                                             the_35_game, themes_game, tord_kb, nie_kb,
#                                             the_35_kb, themes_kb, chat_id, chat_type,
#                                             username, fName, lName, is_bot)
#                                             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#                         """
#             data = (user_id, lang_code, tord_game, nie_game,
#                     the_35_game, themes_game, tord_kb, nie_kb,
#                     the_35_kb, themes_kb, chat_id, chat_type,
#                     username, fName, lName, is_bot)
#             cursor.execute(query, data)
#
#             user_objects[user_id] = users_obj  # ADD OBJECT TO OBJECT DICT
#
#             connection.commit()
#             connection.close()
#         else:
#             user_objects[user_id] = users_obj  # ADD OBJECT TO OBJECT DICT
#             connection.close()
#
#     @classmethod
#     def get_user_obj_from_db(cls, the_user_id: str | int):
#         connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database="users", port=DB_PORT)
#         cursor = connection.cursor()
#
#         query = "SELECT * FROM users WHERE user_id = ?"
#         cursor.execute(query, (the_user_id,))
#         data = cursor.fetchall()
#
#         # the_dict = {
#         #     "user_id": data[0][0],
#         #     "lang_code": data[0][1],
#         #     "tord_game": pickle.loads(data[0][2]),
#         #     "nie_game": pickle.loads(data[0][3]),
#         #     "the_35_game": pickle.loads(data[0][4]),
#         #     "themes_game": pickle.loads(data[0][5]),
#         #     "tord_kb": pickle.loads(data[0][6]),
#         #     "nie_kb": pickle.loads(data[0][7]),
#         #     "the_35_kb": pickle.loads(data[0][8]),
#         #     "themes_kb": pickle.loads(data[0][9]),
#         #     "chat_id": data[0][10],
#         #     "chat_type": data[0][11],
#         #     "username": data[0][12],
#         #     "fName": data[0][13],
#         #     "lName": data[0][14],
#         #     "is_bot": data[0][15]
#         # }
#
#         return_obj = Users(data[0][0],
#                            data[0][1],
#                            pickle.loads(data[0][2]),
#                            pickle.loads(data[0][3]),
#                            pickle.loads(data[0][4]),
#                            pickle.loads(data[0][5]),
#                            pickle.loads(data[0][6]),
#                            pickle.loads(data[0][7]),
#                            pickle.loads(data[0][8]),
#                            pickle.loads(data[0][9]),
#                            data[0][10],
#                            data[0][11],
#                            data[0][12],
#                            data[0][13],
#                            data[0][14],
#                            data[0][15])
#
#         return return_obj
#
#     @classmethod
#     def update_user_obj(cls, the_user_id, new_obj):
#         user_id = new_obj.user_id
#         lang_code = new_obj.lang_code
#
#         tord_game = pickle.dumps(new_obj.tord_game)
#         nie_game = pickle.dumps(new_obj.nie_game)
#         the_35_game = pickle.dumps(new_obj.the_35_game)
#         themes_game = pickle.dumps(new_obj.themes_game)
#
#         tord_kb = pickle.dumps(new_obj.tord_kb)
#         nie_kb = pickle.dumps(new_obj.nie_kb)
#         the_35_kb = pickle.dumps(new_obj.the_35_kb)
#         themes_kb = pickle.dumps(new_obj.themes_kb)
#
#         chat_id = new_obj.chat_id
#         chat_type = new_obj.chat_type
#         username = new_obj.username
#         fName = new_obj.fName
#         lName = new_obj.lName
#         is_bot = int(new_obj.is_bot)
#
#         connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database="users", port=DB_PORT)
#         cursor = connection.cursor()
#
#         query = """UPDATE users SET user_id = ?, lang_code = ?, tord_game = ?, nie_game = ?,
#             the_35_game = ?, themes_game = ?, tord_kb = ?, nie_kb = ?,
#             the_35_kb = ?, themes_kb = ?, chat_id = ?, chat_type = ?,
#             username = ?, fName = ?, lName = ?, is_bot = ?
#             WHERE user_id = ?"""
#
#         cursor.execute(query, (user_id, lang_code, tord_game, nie_game,
#                                the_35_game, themes_game, tord_kb, nie_kb,
#                                the_35_kb, themes_kb, chat_id, chat_type,
#                                username, fName, lName, is_bot,
#                                the_user_id,))
#
#         user_objects[user_id] = new_obj  # UPDATE OBJECT IN OBJECT DICT
#
#         connection.commit()
#         connection.close()
#
#     @classmethod
#     def retrieve_user_obj(cls, user_id):
#         try:
#             user_obj = user_objects[user_id]
#         except KeyError:
#             user_objects[user_id] = cls.get_user_obj_from_db(user_id)
#             user_obj = user_objects[user_id]
#
#         return user_obj
#
#     @classmethod
#     def chat_ids(cls):
#         connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database="users",port=DB_PORT)
#         cursor = connection.cursor()
#         query = """SELECT chat_id FROM USERS;"""
#         cursor.execute(query)
#         rows = cursor.fetchall()
#         users_list = []
#         for row in rows:
#             users_list.append(row)
#
#         connection.commit()
#         connection.close()
#
#         return users_list
#
#     @classmethod
#     def get_user_lang_code(cls, user_id):
#         connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database="users",port=DB_PORT)
#         cursor = connection.cursor()
#
#         query = """SELECT lang_code FROM USERS WHERE user_id = ?"""
#         cursor.execute(query, (user_id,))
#         lang_code = cursor.fetchone()[0]
#
#         connection.commit()
#         connection.close()
#
#         return str(lang_code)
#
#     @classmethod
#     def change_user_lang_code(cls, lang_code, user_id):
#         connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database="users", port=DB_PORT)
#         cursor = connection.cursor()
#
#         query = "UPDATE users SET lang_code = ? WHERE user_id = ?"
#         data = (lang_code, user_id)
#         cursor.execute(query, data)
#
#         connection.commit()
#         connection.close()
#
#     @classmethod
#     def get_statistics(cls):
#         connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database="users", port=DB_PORT)
#         cursor = connection.cursor()
#
#         cursor.execute("SELECT user_id FROM users")
#         all_users_number = len(cursor.fetchall())
#
#         cursor.execute("SELECT * FROM users WHERE lang_code = ru")
#         ru_users_number = len(cursor.fetchall())
#
#         cursor.execute("SELECT * FROM users WHERE lang_code = uk")
#         uk_users_number = len(cursor.fetchall())
#
#         cursor.execute("SELECT * FROM users WHERE lang_code = en")
#         en_users_number = len(cursor.fetchall())
#
#         cursor.execute("SELECT * FROM users WHERE lang_code = de")
#         de_users_number = len(cursor.fetchall())
#
#         cursor.execute("SELECT * FROM users WHERE lang_code = es")
#         es_users_number = len(cursor.fetchall())
#
#         cursor.execute("SELECT * FROM users WHERE lang_code = fr")
#         fr_users_number = len(cursor.fetchall())
#
#         cursor.execute("SELECT * FROM users WHERE lang_code = sr")
#         sr_users_number = len(cursor.fetchall())
#
#         data = {
#             "all": all_users_number,
#             "ru": ru_users_number,
#             "uk": uk_users_number,
#             "en": en_users_number,
#             "de": de_users_number,
#             "es": es_users_number,
#             "fr": fr_users_number,
#             "sr": sr_users_number
#         }
#
#         connection.commit()
#         connection.close()
#
#         return data
#
#

import psycopg2
from mainUnit.config import DB_HOST, DB_PORT, DB_USERNAME, DB_PWD, DB_NAME

def create_database_if_not_exists():
    try:
        connection = psycopg2.connect(dbname="postgres", user=DB_USERNAME, password=DB_PWD, host=DB_HOST, port=DB_PORT)
        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute(""" CREATE database sintia """)
        print("[INFO] Database 'sintia' has been successfuly created!")

        connection.commit()
        connection.close()
    except psycopg2.errors.DuplicateDatabase:
        print("[WARNING] Database 'sitnia' already exists!")

create_database_if_not_exists()