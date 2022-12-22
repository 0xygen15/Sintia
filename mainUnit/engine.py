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
        levels = [lifestyle, absurd, relations, personal, adult]

        def check_and_add(level):
            if level == True:
                for item in lists:
                    adder(item[0], level, item[1])
            else:
                pass

        for level in levels:
            check_and_add(level)


        for _ in [self.t_all, self.d_all, self.n_all]:
            random.shuffle(_)
            random.shuffle(_)
            random.shuffle(_)


    def three_of_five(self):
        def one_level(filename, levelname):
            with open(f"database/{filename}", mode="r", encoding="utf8") as f:
                file = json.load(f)
                levelfile_dict = file[levelname]
                levelfile_list = [value for value in levelfile_dict.values()]
                random.shuffle(levelfile_list)
                return levelfile_list[0:5]

        levels = ["lifestyle", "absurd", "relations", "personal", "adult"]
        files = ["truth.json", "dare.json", "never.json"]

        truth = {}
        dare = {}
        never = {}

        for level in levels:
            truth[level] = one_level(files[0], level)
            dare[level] = one_level(files[1], level)
            never[level] = one_level(files[2], level)

        return

