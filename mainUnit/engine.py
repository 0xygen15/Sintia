import random
import json

import sqlite3

class Engine:
    def __init__(self):
        # These lists are supposed to nest chosen level`s questions from low, middle or high lists.
        self.t_all = []
        self.d_all = []
        self.n_all = []

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
            with open(f"database/{filename}", mode="r", encoding="utf8") as f:
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
            with open(f"database/{filename}", mode="r", encoding="utf8") as f:
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
        with open(f"database/themes_truth.json", mode="r", encoding="utf8") as f:
            file = json.load(f)
            names = [k for k, v in file.items()]
            return names

    def theme(self, theme_name: str):
        with open(f"database/themes_truth.json", mode="r", encoding="utf8") as f:
            file = json.load(f)
            theme_questions_dict = file[theme_name]
        theme_questions_list = [v for k, v in theme_questions_dict.items()]
        return theme_questions_list

class Users:
    connection = sqlite3.connect("./database/users.db")
    c = connection.cursor()

    @classmethod
    def create_table(cls):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            chat_id CHAR NOT NULL UNIQUE,
            chat_type CHAR NOT NULL,
            username CHAR NOT NULL,
            fName CHAR NOT NULL,
            lName CHAR NOT NULL,
            user_id CHAR NOT NULL UNIQUE,
            language_code CHAR NOT NULL,
            is_bot INT NOT NULL
        );
        """
        cls.c.execute(query)
        cls.connection.commit()

    @classmethod
    def create(cls, data: dict):
        query = """
        INSERT INTO USERS (chat_id, chat_type, username, fName, lName, user_id, language_code, is_bot)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        cls.c.execute(query, (data["chat_id"],
                               data["chat_type"],
                               data["username"],
                               data["fName"],
                               data["lName"],
                               data["user_id"],
                               data["language_code"],
                               data["is_bot"])),
        cls.connection.commit()
        cls.connection.close()

    @classmethod
    def chat_ids(cls):
        query = """
        SELECT chat_id, chat_type, username, fName, lName, user_id, language_code, is_bot
        FROM USERS;
        """
        cls.c.execute(query)
        rows = cls.c.fetchall()
        users_list = []
        for row in rows:
            chat_id = int(row[0])
            user_id = int(row[5])

            user_data = {
                'chat_id': chat_id,
                'chat_type': row[1],
                'username': row[2],
                'fName': row[3],
                'lName': row[4],
                'user_id': user_id,
                'language_code': row[6],
                'is_bot': row[7]
            }

            users_list.append(user_data)

        cls.connection.commit()
        cls.connection.close()

        return users_list
