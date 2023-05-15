import random
import json

class Tord:
    def __init__(self, user_id: str | int, lang_code: str):
        self.user_id = user_id
        self.lang_code = lang_code

        self.truths_list = []
        self.dares_list = []

        self.lifestyle_level = False
        self.absurd_level = False
        self.company_level = False
        self.relations_level = False
        self.awkward_level = False

        self.players_list = []
        self.current_player_number = 0
        self.players_number = 0
        self.truth_circle = True
        self.penalties = {}

        self.players_are_added = False
        self.levels_are_chosen = False

        self.truth = ""
        self.dare = ""
        self.current_player_name = ""
        self.first_message_id: int = 0
        self.last_message_id: int = 0

        self.td_obj = ""
        self.td_obj_truth = True

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
                  [self.company_level, "relations"],
                  [self.relations_level, "personal"],
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
                name_capitalised = name.capitalize()
                names_list.append(name_capitalised)
            else:
                names_list.append(name)

        self.players_list = names_list
        self.players_number = len(self.players_list)

        for player in self.players_list:
            self.penalties[player] = 0

    def get_str_of_players_list(self):
        string_names: str = ""
        for name in self.players_list:
            string_names += name
            string_names += ", "
        size = len(string_names)
        string_names = string_names[:size - 2]
        string_names += "."

        return string_names

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
        fail_number = self.penalties[name]
        if 0 <= fail_number < 5:
            pass
        elif fail_number % 5 == 0:
            return True
        else:
            return False

    def load_again(self):
        self.truths_list = []
        self.dares_list = []

        self.set_levels()

    def reset(self):
        self.truths_list = []
        self.dares_list = []

        self.lifestyle_level = False
        self.absurd_level = False
        self.company_level = False
        self.relations_level = False
        self.awkward_level = False

        self.players_list = []
        self.current_player_number = 0
        self.players_number = 0
        self.truth_circle = True
        self.penalties = {}

        self.players_are_added = False
        self.levels_are_chosen = False

        self.truth = ""
        self.dare = ""
        self.current_player_name = ""
        self.first_message_id = ""
        self.last_message_id = ""

        self.td_obj = ""
        self.td_obj_truth = True


class Nie:
    def __init__(self, user_id, lang_code):
        self.user_id = user_id
        self.lang_code = lang_code

        self.truths_list = []
        self.dares_list = []
        self.nevers_list = []

        self.lifestyle_level = False
        self.absurd_level = False
        self.company_level = False
        self.relations_level = False
        self.awkward_level = False

        self.players_list = []
        self.current_player_number = 0
        self.players_number = 0
        self.truth_circle = True
        self.penalties = {}

        self.tord_truth = True
        self.tord = ""
        self.nie = ""

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
                  [self.company_level, "relations"],
                  [self.relations_level, "personal"],
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

    def reset(self):
        self.truths_list = []
        self.dares_list = []
        self.nevers_list = []

        self.lifestyle_level = False
        self.absurd_level = False
        self.company_level = False
        self.relations_level = False
        self.awkward_level = False

        self.players_list = []
        self.current_player_number = 0
        self.players_number = 0
        self.truth_circle = True
        self.penalties = {}

        self.tord_truth = True
        self.tord = ""
        self.nie = ""

class ThreeOfFive:
    def __init__(self, user_id, lang_code):
        self.user_id = user_id
        self.lang_code = lang_code

        self.truths_str = ""
        self.dares_str = ""
        self.nevers_str = ""

        # self.game_dict = {}
        self.game_list: list[str] = []
        self.index: int = 0

    def __str__(self):
        return f"ThreeOfFive object with id: {self.user_id}"

    def main_func(self):
        def list_to_string(the_list):
            the_string = ""
            for item in the_list:
                the_string += item
                the_string += "\n"
            return the_string
        def one_level(filename, levelname):

            with open(f"database/{self.lang_code}/{filename}", mode="r", encoding="utf8") as f:
                file = json.load(f)
                levelfile_dict = file[levelname]
                levelfile_list = [value for value in levelfile_dict.values()]
                random.shuffle(levelfile_list)
                return levelfile_list[0:5]

        levels = [["lifestyle", "1"], ["absurd", "2"], ["relations", "3"], ["personal", "4"], ["adult", "5"]]
        files = ["truth.json", "dare.json", "never.json"]

        for file in files:
            for level in levels:
                file_name = file.split(sep=".")[0]
                text = list_to_string(one_level(file, level[0]))
                # self.game_dict[f"{file_name}{level[1]}"] = text
                self.game_list.append(text)

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

    def reset(self):
        self.truths_str = ""
        self.dares_str = ""
        self.nevers_str = ""
        self.game_list = []

class Themes:
    def __init__(self, user_id, lang_code):
        self.user_id = user_id
        self.lang_code = lang_code

        self.theme_questions_list = []

        self.theme_chosen = ""
        self.index: int

    def __str__(self):
        return f"Themes object with id: {self.user_id}"

    def theme(self):
        with open(f"database/{self.lang_code}/themes_truth.json", mode="r", encoding="utf8") as f:
            file = json.load(f)
            theme_questions_dict = file[self.theme_chosen]
        self.theme_questions_list = [v for k, v in theme_questions_dict.items()]











