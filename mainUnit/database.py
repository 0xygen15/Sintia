# import sqlite3
# import pickle
#
# from mainUnit.users import Users, user_objects
#
#
# class Database:
#     @classmethod
#     def chat_ids(cls):
#         connection = sqlite3.connect("./database/users.db")
#         c = connection.cursor()
#         query = """SELECT chat_id FROM USERS;"""
#         c.execute(query)
#         rows = c.fetchall()
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
#         connection = sqlite3.connect("./database/users.db")
#         c = connection.cursor()
#
#         query = """SELECT lang_code FROM USERS WHERE user_id = %s"""
#         c.execute(query, (user_id,))
#         lang_code = c.fetchone()[0]
#
#         connection.commit()
#         connection.close()
#
#         return str(lang_code)
#
#     @classmethod
#     def change_user_lang_code(cls, lang_code, user_id):
#         connection = sqlite3.connect("./database/users.db")
#         c = connection.cursor()
#
#         query = "UPDATE users SET lang_code = %s WHERE user_id = %s"
#         data = (lang_code, user_id)
#         c.execute(query, data)
#
#         connection.commit()
#         connection.close()
#
#     @classmethod
#     def get_statistics(cls):
#         connection = sqlite3.connect("./database/users.db")
#         c = connection.cursor()
#
#         c.execute("SELECT user_id FROM users")
#         all_users_number = len(c.fetchall())
#
#         c.execute("SELECT * FROM users WHERE lang_code = ru")
#         ru_users_number = len(c.fetchall())
#
#         c.execute("SELECT * FROM users WHERE lang_code = uk")
#         uk_users_number = len(c.fetchall())
#
#         c.execute("SELECT * FROM users WHERE lang_code = en")
#         en_users_number = len(c.fetchall())
#
#         c.execute("SELECT * FROM users WHERE lang_code = de")
#         de_users_number = len(c.fetchall())
#
#         c.execute("SELECT * FROM users WHERE lang_code = es")
#         es_users_number = len(c.fetchall())
#
#         c.execute("SELECT * FROM users WHERE lang_code = fr")
#         fr_users_number = len(c.fetchall())
#
#         c.execute("SELECT * FROM users WHERE lang_code = sr")
#         sr_users_number = len(c.fetchall())
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
#     @classmethod
#     def create_users_db(cls):
#         connection = sqlite3.connect("./database/users.db")
#         c = connection.cursor()
#
#         query = """
#         CREATE TABLE IF NOT EXISTS users (
#         user_id CHAR UNIQUE,
#         lang_code CHAR,
#         tord_game BYTEA,
#         nie_game BYTEA,
#         the_35_game BYTEA,
#         themes_game BYTEA,
#         tord_kb BYTEA,
#         nie_kb BYTEA,
#         the_35_kb BYTEA,
#         themes_kb BYTEA,
#         chat_id CHAR,
#         chat_type CHAR,
#         username CHAR,
#         fName CHAR,
#         lName CHAR,
#         is_bot INTEGER
#         )
#         """
#
#         c.execute(query)
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
#         connection = sqlite3.connect("./database/users.db")
#         c = connection.cursor()
#
#         try:
#             c.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
#             result = c.fetchone()[0]
#         except:
#
#             # if result is None:
#             query = """
#                     INSERT INTO users (user_id, lang_code, tord_game, nie_game,
#                                         the_35_game, themes_game, tord_kb, nie_kb,
#                                         the_35_kb, themes_kb, chat_id, chat_type,
#                                         username, fName, lName, is_bot)
#                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                     """
#             data = (user_id, lang_code, tord_game, nie_game,
#                     the_35_game, themes_game, tord_kb, nie_kb,
#                     the_35_kb, themes_kb, chat_id, chat_type,
#                     username, fName, lName, is_bot)
#             c.execute(query, data)
#
#             user_objects[user_id] = users_obj  # ADD OBJECT TO OBJECT DICT
#
#             connection.commit()
#             connection.close()
#         else:
#             user_objects[user_id] = users_obj  # ADD OBJECT TO OBJECT DICT
#             connection.close()
#
#
#
#     @classmethod
#     def get_user_obj_from_db(cls, the_user_id: str | int):
#         connection = sqlite3.connect("./database/users.db")
#         c = connection.cursor()
#
#         query = "SELECT * FROM users WHERE user_id = %s"
#         c.execute(query, (the_user_id,))
#         data = c.fetchall()
#
#         the_dict = {
#             "user_id": data[0][0],
#             "lang_code": data[0][1],
#             "tord_game": pickle.loads(data[0][2]),
#             "nie_game": pickle.loads(data[0][3]),
#             "the_35_game": pickle.loads(data[0][4]),
#             "themes_game": pickle.loads(data[0][5]),
#             "tord_kb": pickle.loads(data[0][6]),
#             "nie_kb": pickle.loads(data[0][7]),
#             "the_35_kb": pickle.loads(data[0][8]),
#             "themes_kb": pickle.loads(data[0][9]),
#             "chat_id": data[0][10],
#             "chat_type": data[0][11],
#             "username": data[0][12],
#             "fName": data[0][13],
#             "lName": data[0][14],
#             "is_bot":data[0][15]
#         }
#
#         return_obj = Users(data[0][0],
#                             data[0][1],
#                             pickle.loads(data[0][2]),
#                             pickle.loads(data[0][3]),
#                             pickle.loads(data[0][4]),
#                             pickle.loads(data[0][5]),
#                             pickle.loads(data[0][6]),
#                             pickle.loads(data[0][7]),
#                             pickle.loads(data[0][8]),
#                             pickle.loads(data[0][9]),
#                             data[0][10],
#                             data[0][11],
#                             data[0][12],
#                             data[0][13],
#                             data[0][14],
#                             data[0][15])
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
#         connection = sqlite3.connect("./database/users.db")
#         c = connection.cursor()
#
#         query = """UPDATE users SET user_id = %s, lang_code = %s, tord_game = %s, nie_game = %s,
#         the_35_game = %s, themes_game = %s, tord_kb = %s, nie_kb = %s,
#         the_35_kb = %s, themes_kb = %s, chat_id = %s, chat_type = %s,
#         username = %s, fName = %s, lName = %s, is_bot = %s
#         WHERE user_id = %s"""
#
#         c.execute(query, (user_id, lang_code, tord_game, nie_game,
#                           the_35_game, themes_game, tord_kb, nie_kb,
#                           the_35_kb, themes_kb, chat_id, chat_type,
#                           username, fName, lName, is_bot,
#                           the_user_id,))
#
#         user_objects[user_id] = new_obj # UPDATE OBJECT IN OBJECT DICT
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


import psycopg2
import pickle

from mainUnit.config import DB_HOST, DB_PORT, DB_USERNAME, DB_PWD, DB_NAME

from mainUnit.users import Users, user_objects

class Database:
    @classmethod
    def create_database_if_not_exists(cls):
        try:
            connection = psycopg2.connect(dbname="postgres", user=DB_USERNAME, password=DB_PWD, host=DB_HOST, port=DB_PORT)
            connection.autocommit = True
            cursor = connection.cursor()

            cursor.execute(""" CREATE database sintia """)
            print("[INFO] Database 'sintia' has been successfuly created!")

            connection.commit()
            connection.close()
        except psycopg2.errors.DuplicateDatabase:
            print("[INFO] Database 'sintia' already exists, therefore create-script skipped.")
        else:
            cls.create_users_table()


    @classmethod
    def create_users_table(cls):
        connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database=DB_NAME, port=DB_PORT)
        cursor = connection.cursor()

        query = """
            CREATE TABLE IF NOT EXISTS users (
            user_id CHAR(32) UNIQUE,
            lang_code CHAR(3),
            tord_game BYTEA,
            nie_game BYTEA,
            the_35_game BYTEA,
            themes_game BYTEA,
            tord_kb BYTEA,
            nie_kb BYTEA,
            the_35_kb BYTEA,
            themes_kb BYTEA,
            chat_id CHAR(32),
            chat_type CHAR(32),
            username CHAR(255),
            fName CHAR(96),
            lName CHAR(96),
            is_bot SMALLINT
            ) 
            """

        cursor.execute(query)
        print("[INFO] Table 'users' was successfully created in database 'sintia'!")

        connection.commit()
        connection.close()

    @classmethod
    def add_user_to_db(cls, users_obj: Users):
        user_id = users_obj.user_id
        lang_code = users_obj.lang_code

        tord_game = pickle.dumps(users_obj.tord_game)
        nie_game = pickle.dumps(users_obj.nie_game)
        the_35_game = pickle.dumps(users_obj.the_35_game)
        themes_game = pickle.dumps(users_obj.themes_game)

        tord_kb = pickle.dumps(users_obj.tord_kb)
        nie_kb = pickle.dumps(users_obj.nie_kb)
        the_35_kb = pickle.dumps(users_obj.the_35_kb)
        themes_kb = pickle.dumps(users_obj.themes_kb)

        chat_id = users_obj.chat_id
        chat_type = users_obj.chat_type
        username = users_obj.username
        fName = users_obj.fName
        lName = users_obj.lName
        is_bot = int(users_obj.is_bot)

        connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database=DB_NAME, port=DB_PORT)
        print(f"[INFO] Method {cls.add_user_to_db.__name__} connected to database {DB_NAME}.")
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM users WHERE user_id = '%s'", (user_id,))
            print(f"[INFO] Method {cls.add_user_to_db.__name__} has executed SELECT query.")
            result = cursor.fetchone()[0]
            print(f"[INFO] Method {cls.add_user_to_db.__name__}: result fetched")
        except Exception as _ex:
            # if result is None:
            query = """
                        INSERT INTO users (user_id, lang_code, tord_game, nie_game, 
                                            the_35_game, themes_game, tord_kb, nie_kb, 
                                            the_35_kb, themes_kb, chat_id, chat_type, 
                                            username, fName, lName, is_bot) 
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
            data = (user_id, lang_code, tord_game, nie_game,
                    the_35_game, themes_game, tord_kb, nie_kb,
                    the_35_kb, themes_kb, chat_id, chat_type,
                    username, fName, lName, is_bot)
            cursor.execute(query, data)
            print(f"[INFO] Method {cls.add_user_to_db.__name__} has executed INSERT query.")

            user_objects[user_id] = users_obj  # ADD OBJECT TO OBJECT DICT

            connection.commit()
            connection.close()
        else:
            user_objects[user_id] = users_obj  # ADD OBJECT TO OBJECT DICT
            print(f"[INFO] Method {cls.add_user_to_db.__name__} has added object to object dict.")
            connection.close()

    @classmethod
    def get_user_obj_from_db(cls, the_user_id: str | int):
        connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database=DB_NAME, port=DB_PORT)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE user_id = '%s'"
        cursor.execute(query, (the_user_id,))
        data = cursor.fetchall()

        # the_dict = {
        #     "user_id": data[0][0],
        #     "lang_code": data[0][1],
        #     "tord_game": pickle.loads(data[0][2]),
        #     "nie_game": pickle.loads(data[0][3]),
        #     "the_35_game": pickle.loads(data[0][4]),
        #     "themes_game": pickle.loads(data[0][5]),
        #     "tord_kb": pickle.loads(data[0][6]),
        #     "nie_kb": pickle.loads(data[0][7]),
        #     "the_35_kb": pickle.loads(data[0][8]),
        #     "themes_kb": pickle.loads(data[0][9]),
        #     "chat_id": data[0][10],
        #     "chat_type": data[0][11],
        #     "username": data[0][12],
        #     "fName": data[0][13],
        #     "lName": data[0][14],
        #     "is_bot": data[0][15]
        # }

        return_obj = Users(data[0][0],
                           data[0][1],
                           pickle.loads(data[0][2]),
                           pickle.loads(data[0][3]),
                           pickle.loads(data[0][4]),
                           pickle.loads(data[0][5]),
                           pickle.loads(data[0][6]),
                           pickle.loads(data[0][7]),
                           pickle.loads(data[0][8]),
                           pickle.loads(data[0][9]),
                           data[0][10],
                           data[0][11],
                           data[0][12],
                           data[0][13],
                           data[0][14],
                           data[0][15])

        return return_obj

    @classmethod
    def update_user_obj(cls, the_user_id, new_obj):
        user_id = new_obj.user_id
        lang_code = new_obj.lang_code

        tord_game = pickle.dumps(new_obj.tord_game)
        nie_game = pickle.dumps(new_obj.nie_game)
        the_35_game = pickle.dumps(new_obj.the_35_game)
        themes_game = pickle.dumps(new_obj.themes_game)

        tord_kb = pickle.dumps(new_obj.tord_kb)
        nie_kb = pickle.dumps(new_obj.nie_kb)
        the_35_kb = pickle.dumps(new_obj.the_35_kb)
        themes_kb = pickle.dumps(new_obj.themes_kb)

        chat_id = new_obj.chat_id
        chat_type = new_obj.chat_type
        username = new_obj.username
        fName = new_obj.fName
        lName = new_obj.lName
        is_bot = int(new_obj.is_bot)

        connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database=DB_NAME, port=DB_PORT)
        cursor = connection.cursor()

        query = """UPDATE users SET user_id = %s, lang_code = %s, tord_game = %s, nie_game = %s, 
            the_35_game = %s, themes_game = %s, tord_kb = %s, nie_kb = %s, 
            the_35_kb = %s, themes_kb = %s, chat_id = %s, chat_type = %s, 
            username = %s, fName = %s, lName = %s, is_bot = %s
            WHERE user_id = %s"""

        cursor.execute(query, (user_id, lang_code, tord_game, nie_game,
                               the_35_game, themes_game, tord_kb, nie_kb,
                               the_35_kb, themes_kb, chat_id, chat_type,
                               username, fName, lName, is_bot,
                               the_user_id,))

        user_objects[user_id] = new_obj  # UPDATE OBJECT IN OBJECT DICT

        connection.commit()
        connection.close()

    @classmethod
    def retrieve_user_obj(cls, user_id):
        try:
            user_obj = user_objects[user_id]
        except KeyError:
            user_objects[user_id] = cls.get_user_obj_from_db(user_id)
            user_obj = user_objects[user_id]

        return user_obj

    @classmethod
    def chat_ids(cls):
        connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database=DB_NAME,port=DB_PORT)
        cursor = connection.cursor()
        query = """SELECT chat_id FROM USERS;"""
        cursor.execute(query)
        rows = cursor.fetchall()
        users_list = []
        for row in rows:
            users_list.append(row)

        connection.commit()
        connection.close()

        return users_list

    @classmethod
    def get_user_lang_code(cls, user_id):
        connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database=DB_NAME,port=DB_PORT)
        cursor = connection.cursor()

        query = """SELECT lang_code FROM USERS WHERE user_id = '%s'"""
        cursor.execute(query, (user_id,))
        lang_code = cursor.fetchone()[0]

        connection.commit()
        connection.close()

        return str(lang_code)

    @classmethod
    def change_user_lang_code(cls, lang_code, user_id):
        connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database=DB_NAME, port=DB_PORT)
        cursor = connection.cursor()

        query = "UPDATE users SET lang_code = %s WHERE user_id = '%s'"
        data = (lang_code, user_id)
        cursor.execute(query, data)

        connection.commit()
        connection.close()

    @classmethod
    def get_statistics(cls):
        connection = psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PWD, database=DB_NAME, port=DB_PORT)
        cursor = connection.cursor()

        cursor.execute("SELECT user_id FROM users")
        all_users_number = len(cursor.fetchall())

        cursor.execute("SELECT * FROM users WHERE lang_code = 'ru'")
        ru_users_number = len(cursor.fetchall())

        cursor.execute("SELECT * FROM users WHERE lang_code = 'uk'")
        uk_users_number = len(cursor.fetchall())

        cursor.execute("SELECT * FROM users WHERE lang_code = 'en'")
        en_users_number = len(cursor.fetchall())

        cursor.execute("SELECT * FROM users WHERE lang_code = 'de'")
        de_users_number = len(cursor.fetchall())

        cursor.execute("SELECT * FROM users WHERE lang_code = 'es'")
        es_users_number = len(cursor.fetchall())

        cursor.execute("SELECT * FROM users WHERE lang_code = 'fr'")
        fr_users_number = len(cursor.fetchall())

        cursor.execute("SELECT * FROM users WHERE lang_code = 'sr'")
        sr_users_number = len(cursor.fetchall())

        data = {
            "all": all_users_number,
            "ru": ru_users_number,
            "uk": uk_users_number,
            "en": en_users_number,
            "de": de_users_number,
            "es": es_users_number,
            "fr": fr_users_number,
            "sr": sr_users_number
        }

        connection.commit()
        connection.close()

        return data