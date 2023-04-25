import random
import json
import sqlite3

class Engine:
    def __init__(self):
        # These lists are supposed to nest chosen level`s questions from low, middle or high lists.
        self.t_all = []
        self.d_all = []
        self.n_all = []

        self.lang_code = ""

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

class Tord:
    def __init__(self, user_id, lang_code):
        self.user_id = user_id
        self.lang_code = lang_code

        self.truths_list = []
        self.dares_list = []

        self.lifestyle_level = False
        self.absurd_level = False
        self.relations_level = False
        self.personal_level = False
        self.awkward_level = False

        self.players_list = []
        self.current_player_number = 0
        self.players_number = 0
        self.truth_circle = True
        self.penalties = {}

    def __str__(self):
        return f"Tord object with id: {self.user_id}"

    def shuffle_lists(self):
        data_lists = [self.truths_list, self.dares_list]
        for the_list in data_lists:
            random.shuffle(the_list)
            random.shuffle(the_list)
            random.shuffle(the_list)

    def out_of_objects(self):
        if len(self.truths_list) == 0 or len(self.dares_list) == 0:
            return True
        else:
            return False

    def set_levels(self):
        def file(filename):
            with open(f"database/{self.lang_code}/{filename}", mode="r", encoding="utf8") as f:
                return json.load(f)

        def adder(file, level, qlist):
            for key, value in file[level].items():
                qlist.append(value)

        files_and_status = [[file("truth.json"), self.truths_list],
                            [file("dare.json"), self.dares_list]]

        levels = [[self.lifestyle_level, "lifestyle"],
                  [self.absurd_level, "absurd"],
                  [self.relations_level, "relations"],
                  [self.personal_level, "personal"],
                  [self.awkward_level, "adult"]]


        for level in levels:
            if level[0]:
                for file_and_status in files_and_status:
                    adder(file_and_status[0], level[1], file_and_status[1])
            else:
                pass


        for the_list in [self.truths_list, self.dares_list]:
            random.shuffle(the_list)
            random.shuffle(the_list)
            random.shuffle(the_list)

    def add_players_names(self, data: str):
        """
        The function returns a list of names from a raw string where names are separated with commas.
        """
        raw_names_list = data.split(sep=",")
        names_list = []
        for raw_name in raw_names_list:
            name = (raw_name.replace(" ", ""))
            if name.islower():
                name.capitalize()
            else:
                pass
            names_list.append(name)
        self.players_list = names_list
        self.players_number = len(self.players_list)

        for player in self.players_list:
            self.penalties[player] = 0

    def next_player_number(self):
        """
        The function updates the variable 'self.current_player_number' increasing it by 1.
        """
        self.current_player_number += 1
        if self.current_player_number == len(self.players_list):
            self.current_player_number = 0

    def circle_changer(self):
        if self.current_player_number == 0:
            if self.truth_circle:
                self.truth_circle = False
            elif not self.truth_circle:
                self.truth_circle = True

    def fail_check(self, name):
        fail_number = self.penalties[name]['p']
        if 0 <= fail_number < 5:
            pass
        elif fail_number % 5 == 0:
            return True
        else:
            return False

class Nie:
    def __init__(self, user_id, lang_code):
        self.user_id = user_id
        self.lang_code = lang_code

        self.truths_list = []
        self.dares_list = []
        self.nevers_list = []

        self.lifestyle_level = False
        self.absurd_level = False
        self.relations_level = False
        self.personal_level = False
        self.awkward_level = False

        self.players_list = []
        self.current_player_number = 0
        self.players_number = 0
        self.truth_circle = True
        self.penalties = {}

    def __str__(self):
        return f"Nie object with id: {self.user_id}"

    def shuffle_lists(self):
        data_lists = [self.truths_list, self.dares_list, self.nevers_list]
        for the_list in data_lists:
            random.shuffle(the_list)
            random.shuffle(the_list)
            random.shuffle(the_list)

    def out_of_objects(self):
        if len(self.truths_list) == 0 or len(self.dares_list) == 0 or len(self.nevers_list) == 0:
            return True
        else:
            return False

    def set_levels(self):
        def file(filename):
            with open(f"database/{self.lang_code}/{filename}", mode="r", encoding="utf8") as f:
                return json.load(f)

        def adder(file, level, qlist):
            for key, value in file[level].items():
                qlist.append(value)

        files_and_status = [[file("truth.json"), self.truths_list],
                            [file("dare.json"), self.dares_list],
                            [file("never.json"), self.nevers_list]]

        levels = [[self.lifestyle_level, "lifestyle"],
                  [self.absurd_level, "absurd"],
                  [self.relations_level, "relations"],
                  [self.personal_level, "personal"],
                  [self.awkward_level, "adult"]]


        for level in levels:
            if level[0]:
                for file_and_status in files_and_status:
                    adder(file_and_status[0], level[1], file_and_status[1])
            else:
                pass


        for the_list in [self.truths_list, self.dares_list]:
            random.shuffle(the_list)
            random.shuffle(the_list)
            random.shuffle(the_list)

class ThreeOfFive:
    def __init__(self, user_id, lang_code):
        self.user_id = user_id
        self.lang_code = lang_code

        self.truths_str = ""
        self.dares_str = ""
        self.nevers_str = ""

    def __str__(self):
        return f"ThreeOfFive object with id: {self.user_id}"

    def three_of_five(self):
        def one_level(filename, levelname):

            with open(f"database/{self.lang_code}/{filename}", mode="r", encoding="utf8") as f:
                file = json.load(f)
                levelfile_dict = file[levelname]
                levelfile_list = [value for value in levelfile_dict.values()]
                random.shuffle(levelfile_list)
                return levelfile_list[0:5]

        def list_to_string(the_list):
            the_string = ""
            for item in the_list:
                the_string += item
                the_string += "\n"
            return the_string

        levels = [["lifestyle", "1"], ["absurd", "2"], ["relations", "3"], ["personal", "4"], ["adult", "5"]]
        files = ["truth.json", "dare.json", "never.json"]

        self.truths_str = ""
        self.dares_str = ""
        self.nevers_str = ""

        for level in levels:
            self.truths_str += f"<b>{level[1]}:</b>\n"
            self.truths_str += f"{list_to_string(the_list=one_level(files[0], level[0]))}\n"
            self.dares_str += f"<b>{level[1]}:</b>\n"
            self.dares_str += f"{list_to_string(the_list=one_level(files[1], level[0]))}\n"
            self.nevers_str += f"<b>{level[1]}:</b>\n"
            self.nevers_str += f"{list_to_string(the_list=one_level(files[2], level[0]))}\n"

class Themes:
    def __init__(self, user_id, lang_code):
        self.user_id = user_id
        self.lang_code = lang_code

        self.theme_questions_list = []

    def __str__(self):
        return f"Themes object with id: {self.user_id}"

    def theme(self, theme_name: str):
        with open(f"database/{self.lang_code}/themes_truth.json", mode="r", encoding="utf8") as f:
            file = json.load(f)
            theme_questions_dict = file[theme_name]
        self.theme_questions_list = [v for k, v in theme_questions_dict.items()]