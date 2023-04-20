import random
import json

import sqlite3

from local.lang import Texts

class Engine:
    def __init__(self):
        # These lists are supposed to nest chosen level`s questions from low, middle or high lists.
        self.t_all = []
        self.d_all = []
        self.n_all = []

        self.lang_code = Texts.lang_code

    def shuffled_list(self, object: list):
        import random
        random.shuffle(object)
        random.shuffle(object)
        random.shuffle(object)
        return object

    def out_of_objects(self, object: list):
        if len(object) == 0:
            return True
        else:
            return False

    def set_levels(self, lifestyle, absurd, relations, personal, adult):
        def file(filename):
            with open(f"database/{self.lang_code}/{filename}", mode="r", encoding="utf8") as f:
                return json.load(f)

        def adder(file, level, qlist):
            for key, value in file[level].items():
                qlist.append(value)

        lists = [[file("truth.json"), self.t_all], [file("dare.json"), self.d_all], [file("never.json"), self.n_all]]
        levels = [[lifestyle, "lifestyle"], [absurd, "absurd"], [relations, "relations"], [personal, "personal"], [adult, "adult"]]

        def check_and_add(level):
            if level[0] == True:
                for item in lists:
                    adder(item[0], level[1], item[1])
            else:
                pass

        for level in levels:
            check_and_add(level)


        for _ in [self.t_all, self.d_all, self.n_all]:
            random.shuffle(_)
            random.shuffle(_)
            random.shuffle(_)

    def list_to_string(self, the_list):
        the_string = ""
        for item in the_list:
            the_string += item
            the_string += "\n"
        return the_string

    def three_of_five(self):
        def one_level(filename, levelname):
            with open(f"database/{self.lang_code}/{filename}", mode="r", encoding="utf8") as f:
                file = json.load(f)
                levelfile_dict = file[levelname]
                levelfile_list = [value for value in levelfile_dict.values()]
                random.shuffle(levelfile_list)
                return levelfile_list[0:5]

        levels = [["lifestyle", "1"], ["absurd", "2"], ["relations", "3"], ["personal", "4"], ["adult", "5"]]
        files = ["truth.json", "dare.json", "never.json"]

        truth = ""
        dare = ""
        never = ""

        for level in levels:
            truth += f"<b>{level[1]}:</b>\n"
            truth += f"{Engine.list_to_string(self, the_list=one_level(files[0], level[0]))}\n"
            dare += f"<b>{level[1]}:</b>\n"
            dare += f"{Engine.list_to_string(self, the_list=one_level(files[1], level[0]))}\n"
            never += f"<b>{level[1]}:</b>\n"
            never += f"{Engine.list_to_string(self, the_list=one_level(files[2], level[0]))}\n"

        return [truth, dare, never]

    def theme_names(self):
        with open(f"database/{self.lang_code}/themes_truth.json", mode="r", encoding="utf8") as f:
            file = json.load(f)
            names = [k for k, v in file.items()]
            return names

    def theme(self, theme_name: str):
        with open(f"database/{self.lang_code}/themes_truth.json", mode="r", encoding="utf8") as f:
            file = json.load(f)
            theme_questions_dict = file[theme_name]
        theme_questions_list = [v for k, v in theme_questions_dict.items()]
        return theme_questions_list

class Users:
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

        return data
