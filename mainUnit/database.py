import sqlite3
import pickle

class Database:
    # connection = sqlite3.connect("./database/users.db")
    # c = connection.cursor()

    @classmethod
    def create_table(cls):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS users (
            chat_id CHAR NOT NULL UNIQUE,
            chat_type CHAR NOT NULL,
            username CHAR NOT NULL,
            fName CHAR,
            lName CHAR,
            user_id CHAR NOT NULL UNIQUE,
            language_code CHAR NOT NULL,
            is_bot INT NOT NULL
        );
        """
        # cls.c.execute(query)
        # cls.connection.commit()
        c.execute(query)
        connection.commit()

    @classmethod
    def create(cls, data: dict):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute("SELECT * FROM users WHERE user_id = ?", (data["user_id"],))
        result = c.fetchone()

        if result is None:
            query = """
                    INSERT INTO USERS (chat_id, chat_type, username, fName, lName, user_id, language_code, is_bot)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                    """

            c.execute(query, (data["chat_id"],
                              data["chat_type"],
                              data["username"],
                              data["fName"],
                              data["lName"],
                              data["user_id"],
                              data["language_code"],
                              data["is_bot"])),
            connection.commit()
            connection.close()
        else:
            pass


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

        query = """SELECT language_code FROM USERS WHERE user_id = ?"""
        c.execute(query, (user_id,))
        lang_code = c.fetchone()[0]

        connection.commit()
        connection.close()

        return str(lang_code)

    @classmethod
    def change_user_lang_code(cls, lang_code, user_id):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        query = "UPDATE users SET language_code = ? WHERE user_id = ?"
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

        c.execute("SELECT * FROM users WHERE language_code = ru")
        ru_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE language_code = uk")
        uk_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE language_code = en")
        en_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE language_code = de")
        de_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE language_code = es")
        es_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE language_code = fr")
        fr_users_number = len(c.fetchall())

        c.execute("SELECT * FROM users WHERE language_code = sr")
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

    @classmethod
    def create_tord_obj_table(cls):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS tord_objects (
                        user_id CHAR UNIQUE,
                        language_code CHAR, 
                        tord_obj BLOB,
                        tord_kb_obj BLOB)''')

        connection.commit()
        connection.close()

    @classmethod
    def save_tord_obj_to_bd(cls, user_id, language_code, tord_obj, tord_kb_obj):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        obj_data = pickle.dumps(tord_obj)
        obj_kb_data = pickle.dumps(tord_kb_obj)

        c.execute("INSERT INTO tord_objects (user_id, language_code, tord_obj, tord_kb_obj) VALUES (?, ?, ?, ?)",
                  (user_id, language_code, obj_data, obj_kb_data))

        connection.commit()
        connection.close()

    @classmethod
    def get_tord_obj_from_db(cls, user_id):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute("SELECT tord_obj, tord_kb_obj FROM tord_objects WHERE user_id=?", (user_id,))
        data = c.fetchone()
        tord_obj = pickle.loads(data[0][0])
        tord_kb_obj = pickle.loads(data[0][1])

        return tord_obj, tord_kb_obj

    @classmethod
    def create_nie_obj_table(cls):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS nie_objects (
                            user_id CHAR UNIQUE,
                            language_code CHAR, 
                            nie_obj BLOB,
                            nie_kb_obj BLOB)''')

        connection.commit()
        connection.close()

    @classmethod
    def save_nie_obj_to_bd(cls, user_id, language_code, nie_obj, nie_kb_obj):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        obj_data = pickle.dumps(nie_obj)
        obj_kb_data = pickle.dumps(nie_kb_obj)

        c.execute("INSERT INTO nie_objects (user_id, language_code, nie_obj, nie_kb_obj) VALUES (?, ?, ?, ?)",
                  (user_id, language_code, obj_data, obj_kb_data))

        connection.commit()
        connection.close()

    @classmethod
    def get_nie_obj_from_db(cls, user_id):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute("SELECT nie_obj, nie_kb_obj FROM nie_objects WHERE user_id=?", (user_id,))
        data = c.fetchone()
        nie_obj = pickle.loads(data[0][0])
        nie_kb_obj = pickle.loads(data[0][1])

        return nie_obj, nie_kb_obj

    @classmethod
    def create_nie_obj_table(cls):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS nie_objects (
                                user_id CHAR UNIQUE,
                                language_code CHAR, 
                                nie_obj BLOB,
                                nie_kb_obj BLOB)''')

        connection.commit()
        connection.close()

    @classmethod
    def save_three_of_five_obj_to_bd(cls, user_id, language_code, three_of_five_obj, three_of_five_kb_obj):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        obj_data = pickle.dumps(three_of_five_obj)
        obj_kb_data = pickle.dumps(three_of_five_kb_obj)

        c.execute("INSERT INTO three_of_five_objects (user_id, language_code, three_of_five_obj, three_of_five_kb_obj) VALUES (?, ?, ?, ?)",
                  (user_id, language_code, obj_data, obj_kb_data))

        connection.commit()
        connection.close()

    @classmethod
    def get_three_of_five_obj_from_db(cls, user_id):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute("SELECT three_of_five_obj, three_of_five_kb_obj FROM nie_objects WHERE user_id=?", (user_id,))
        data = c.fetchone()
        three_of_five_obj = pickle.loads(data[0][0])
        three_of_five_kb_obj = pickle.loads(data[0][1])

        return three_of_five_obj, three_of_five_kb_obj

    @classmethod
    def create_themes_obj_table(cls):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS themes_objects (
                                user_id CHAR UNIQUE,
                                language_code CHAR, 
                                themes_obj BLOB,
                                themes_kb_obj BLOB)''')

        connection.commit()
        connection.close()

    @classmethod
    def save_themes_obj_to_bd(cls, user_id, language_code, themes_obj, themes_kb_obj):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        obj_data = pickle.dumps(themes_obj)
        obj_kb_data = pickle.dumps(themes_kb_obj)

        c.execute("INSERT INTO themes_objects (user_id, language_code, themes_obj, themes_kb_obj) VALUES (?, ?, ?, ?)",
                  (user_id, language_code, obj_data, obj_kb_data))

        connection.commit()
        connection.close()

    @classmethod
    def get_themes_obj_from_db(cls, user_id):
        connection = sqlite3.connect("./database/users.db")
        c = connection.cursor()

        c.execute("SELECT themes_obj, themes_kb_obj FROM themes_objects WHERE user_id=?", (user_id,))
        data = c.fetchone()
        themes_obj = pickle.loads(data[0][0])
        themes_kb_obj = pickle.loads(data[0][1])

        return themes_obj, themes_kb_obj



    """
    import sqlite3
    import pickle
    
    class MyClass:
        def __init__(self, name, value):
            self.name = name
            self.value = value
    
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    
    # Define a table schema that includes a BLOB field for the serialized object
    conn.execute('''CREATE TABLE IF NOT EXISTS mytable
                 (name TEXT PRIMARY KEY, obj BLOB)''')
    
    # Create an instance of MyClass
    obj = MyClass('example', 42)
    
    # Serialize the object to binary data using pickle
    obj_data = pickle.dumps(obj)
    
    # Insert the object's binary data into the database
    conn.execute("INSERT INTO mytable (name, obj) VALUES (?, ?)",
                 (obj.name, obj_data))
    
    # Commit the transaction
    conn.commit()
    
    # Retrieve the object from the database
    cursor = conn.execute("SELECT obj FROM mytable WHERE name=?", ('example',))
    row = cursor.fetchone()
    obj2 = pickle.loads(row[0])
    
    # Close the database connection
    conn.close()
    """