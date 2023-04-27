import sqlite3
import pickle

from mainUnit.users import Users, user_objects

import loader

class Database:
    # connection = sqlite3.connect("./database/users.db")
    # c = connection.cursor()

    # @classmethod
    # def create_table(cls):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #     query = """
    #     CREATE TABLE IF NOT EXISTS users (
    #         chat_id CHAR NOT NULL UNIQUE,
    #         chat_type CHAR NOT NULL,
    #         username CHAR NOT NULL,
    #         fName CHAR,
    #         lName CHAR,
    #         user_id CHAR NOT NULL UNIQUE,
    #         language_code CHAR NOT NULL,
    #         is_bot INT NOT NULL
    #     );
    #     """
    #     # cls.c.execute(query)
    #     # cls.connection.commit()
    #     c.execute(query)
    #     connection.commit()
    #
    # @classmethod
    # def create(cls, data: dict):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     c.execute("SELECT * FROM users WHERE user_id = ?", (data["user_id"],))
    #     result = c.fetchone()
    #
    #     if result is None:
    #         query = """
    #                 INSERT INTO USERS (chat_id, chat_type, username, fName, lName, user_id, language_code, is_bot)
    #                 VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    #                 """
    #
    #         c.execute(query, (data["chat_id"],
    #                           data["chat_type"],
    #                           data["username"],
    #                           data["fName"],
    #                           data["lName"],
    #                           data["user_id"],
    #                           data["language_code"],
    #                           data["is_bot"])),
    #         connection.commit()
    #         connection.close()
    #     else:
    #         pass
    @classmethod
    def chat_ids(cls):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()
        query = """SELECT chat_id FROM USERS;"""
        c.execute(query)
        rows = c.fetchall()
        users_list = []
        for row in rows:
            users_list.append(row)

        connection.commit()
        connection.close()

        return users_list

    @classmethod
    def get_user_lang_code(cls, user_id):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        query = """SELECT lang_code FROM USERS WHERE user_id = ?"""
        c.execute(query, (user_id,))
        lang_code = c.fetchone()[0]

        connection.commit()
        connection.close()

        return str(lang_code)

    @classmethod
    def change_user_lang_code(cls, lang_code, user_id):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        query = "UPDATE users SET lang_code = ? WHERE user_id = ?"
        data = (lang_code, user_id)
        c.execute(query, data)

        connection.commit()
        connection.close()

    @classmethod
    def get_statistics(cls):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute("SELECT user_id FROM users")
        all_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE lang_code = ru")
        ru_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE lang_code = uk")
        uk_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE lang_code = en")
        en_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE lang_code = de")
        de_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE lang_code = es")
        es_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE lang_code = fr")
        fr_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE lang_code = sr")
        sr_users_number = len(c.fetchall())

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

    # @classmethod
    # def create_tord_obj_table(cls):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     c.execute('''CREATE TABLE IF NOT EXISTS tord_objects (
    #                     user_id CHAR UNIQUE,
    #                     language_code CHAR,
    #                     tord_obj BLOB,
    #                     tord_kb_obj BLOB)''')
    #
    #     connection.commit()
    #     connection.close()
    #
    # @classmethod
    # def save_tord_obj_to_bd(cls, user_id, language_code, tord_obj, tord_kb_obj):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     obj_data = pickle.dumps(tord_obj)
    #     obj_kb_data = pickle.dumps(tord_kb_obj)
    #
    #     c.execute("INSERT INTO tord_objects (user_id, language_code, tord_obj, tord_kb_obj) VALUES (?, ?, ?, ?)",
    #               (user_id, language_code, obj_data, obj_kb_data))
    #
    #     connection.commit()
    #     connection.close()
    #
    # @classmethod
    # def get_tord_obj_from_db(cls, user_id):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     c.execute("SELECT tord_obj, tord_kb_obj FROM tord_objects WHERE user_id=?", (user_id,))
    #     data = c.fetchone()
    #     tord_obj = pickle.loads(data[0][0])
    #     tord_kb_obj = pickle.loads(data[0][1])
    #
    #     return tord_obj, tord_kb_obj
    #
    # @classmethod
    # def create_nie_obj_table(cls):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     c.execute('''CREATE TABLE IF NOT EXISTS nie_objects (
    #                         user_id CHAR UNIQUE,
    #                         language_code CHAR,
    #                         nie_obj BLOB,
    #                         nie_kb_obj BLOB)''')
    #
    #     connection.commit()
    #     connection.close()
    #
    # @classmethod
    # def save_nie_obj_to_bd(cls, user_id, language_code, nie_obj, nie_kb_obj):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     obj_data = pickle.dumps(nie_obj)
    #     obj_kb_data = pickle.dumps(nie_kb_obj)
    #
    #     c.execute("INSERT INTO nie_objects (user_id, language_code, nie_obj, nie_kb_obj) VALUES (?, ?, ?, ?)",
    #               (user_id, language_code, obj_data, obj_kb_data))
    #
    #     connection.commit()
    #     connection.close()
    #
    # @classmethod
    # def get_nie_obj_from_db(cls, user_id):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     c.execute("SELECT nie_obj, nie_kb_obj FROM nie_objects WHERE user_id=?", (user_id,))
    #     data = c.fetchone()
    #     nie_obj = pickle.loads(data[0][0])
    #     nie_kb_obj = pickle.loads(data[0][1])
    #
    #     return nie_obj, nie_kb_obj
    #
    # @classmethod
    # def create_nie_obj_table(cls):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     c.execute('''CREATE TABLE IF NOT EXISTS nie_objects (
    #                             user_id CHAR UNIQUE,
    #                             language_code CHAR,
    #                             nie_obj BLOB,
    #                             nie_kb_obj BLOB)''')
    #
    #     connection.commit()
    #     connection.close()
    #
    # @classmethod
    # def save_three_of_five_obj_to_bd(cls, user_id, language_code, three_of_five_obj, three_of_five_kb_obj):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     obj_data = pickle.dumps(three_of_five_obj)
    #     obj_kb_data = pickle.dumps(three_of_five_kb_obj)
    #
    #     c.execute("INSERT INTO three_of_five_objects (user_id, language_code, three_of_five_obj, three_of_five_kb_obj) VALUES (?, ?, ?, ?)",
    #               (user_id, language_code, obj_data, obj_kb_data))
    #
    #     connection.commit()
    #     connection.close()
    #
    # @classmethod
    # def get_three_of_five_obj_from_db(cls, user_id):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     c.execute("SELECT three_of_five_obj, three_of_five_kb_obj FROM nie_objects WHERE user_id=?", (user_id,))
    #     data = c.fetchone()
    #     three_of_five_obj = pickle.loads(data[0][0])
    #     three_of_five_kb_obj = pickle.loads(data[0][1])
    #
    #     return three_of_five_obj, three_of_five_kb_obj
    #
    # @classmethod
    # def create_themes_obj_table(cls):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     c.execute('''CREATE TABLE IF NOT EXISTS themes_objects (
    #                             user_id CHAR UNIQUE,
    #                             language_code CHAR,
    #                             themes_obj BLOB,
    #                             themes_kb_obj BLOB)''')
    #
    #     connection.commit()
    #     connection.close()
    #
    # @classmethod
    # def save_themes_obj_to_bd(cls, user_id, language_code, themes_obj, themes_kb_obj):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     obj_data = pickle.dumps(themes_obj)
    #     obj_kb_data = pickle.dumps(themes_kb_obj)
    #
    #     c.execute("INSERT INTO themes_objects (user_id, language_code, themes_obj, themes_kb_obj) VALUES (?, ?, ?, ?)",
    #               (user_id, language_code, obj_data, obj_kb_data))
    #
    #     connection.commit()
    #     connection.close()
    #
    # @classmethod
    # def get_themes_obj_from_db(cls, user_id):
    #     connection = sqlite3.connect("./database/users.db")
    #     c = connection.cursor()
    #
    #     c.execute("SELECT themes_obj, themes_kb_obj FROM themes_objects WHERE user_id=?", (user_id,))
    #     data = c.fetchone()
    #     themes_obj = pickle.loads(data[0][0])
    #     themes_kb_obj = pickle.loads(data[0][1])
    #
    #     return themes_obj, themes_kb_obj

    @classmethod
    def create_users_db(cls):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS users (
        user_id CHAR UNIQUE,
        lang_code CHAR,
        tord_game BLOB,
        nie_game BLOB,
        the_35_game BLOB,
        themes_game BLOB,
        tord_kb BLOB,
        nie_kb BLOB,
        the_35_kb BLOB,
        themes_kb BLOB,
        chat_id CHAR,
        chat_type CHAR,
        username CHAR,
        fName CHAR,
        lName CHAR,
        is_bot INTEGER
        ) 
        """

        c.execute(query)

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

        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        result = c.fetchone()[0]

        if result is None:
            query = """
                    INSERT INTO users (user_id, lang_code, tord_game, nie_game, 
                                        the_35_game, themes_game, tord_kb, nie_kb, 
                                        the_35_kb, themes_kb, chat_id, chat_type, 
                                        username, fName, lName, is_bot) 
                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """
            data = (user_id, lang_code, tord_game, nie_game,
                    the_35_game, themes_game, tord_kb, nie_kb,
                    the_35_kb, themes_kb, chat_id, chat_type,
                    username, fName, lName, is_bot)
            c.execute(query, data)

            user_objects[user_id] = users_obj  # ADD OBJECT TO OBJECT DICT

            connection.commit()
            connection.close()
        else:
            user_objects[user_id] = users_obj  # ADD OBJECT TO OBJECT DICT
            connection.close()



    @classmethod
    def get_user_obj_from_db(cls, the_user_id: Users):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        query = "SELECT * FROM users WHERE user_id = ?"
        c.execute(query, (the_user_id,))
        data = c.fetchall()

        return {
            "user_id": data[0][0],
            "lang_code": data[0][1],
            "tord_game": data[0][2],
            "nie_game": data[0][3],
            "the_35_game": data[0][4],
            "themes_game": data[0][5],
            "tord_kb": data[0][6],
            "nie_kb": data[0][7],
            "the_35_kb": data[0][8],
            "themes_kb": data[0][9],
            "chat_id": data[0][10],
            "chat_type": data[0][11],
            "username": data[0][12],
            "fName": data[0][13],
            "lName": data[0][14],
            "is_bot":data[0][15]
        }

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

        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        query = """UPDATE users SET user_id = ?, lang_code = ?, tord_game = ?, nie_game = ?, 
        the_35_game = ?, themes_game = ?, tord_kb = ?, nie_kb = ?, 
        the_35_kb = ?, themes_kb = ?, chat_id = ?, chat_type = ?, 
        username = ?, fName = ?, lName = ?, is_bot = ?
        WHERE user_id = ?"""

        c.execute(query, (user_id, lang_code, tord_game, nie_game,
                          the_35_game, themes_game, tord_kb, nie_kb,
                          the_35_kb, themes_kb, chat_id, chat_type,
                          username, fName, lName, is_bot,
                          the_user_id,))

        user_objects[user_id] = new_obj # UPDATE OBJECT IN OBJECT DICT

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
