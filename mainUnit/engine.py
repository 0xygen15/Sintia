import random
import json


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



