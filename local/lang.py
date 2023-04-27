import json
import local.key_dicts
# class Texts:
#
#     info = local.key_dicts.info
#     keyboards = local.key_dicts.keyboards
#     never_i_ever = local.key_dicts.never_i_ever
#     themes = local.key_dicts.themes
#     three_of_five = local.key_dicts.three_of_five
#     truth_or_dare = local.key_dicts.truth_or_dare
#
#     handlers_list = [
#         ["info.json", info],
#         ["keyboards.json", keyboards],
#         ["never_i_ever.json", never_i_ever],
#         ["themes.json", themes],
#         ["three_of_five.json", three_of_five],
#         ["truth_or_dare.json", truth_or_dare]]
#
#     lang_code = ""
#
#     @classmethod
#     def load_localisation(cls, lang_code):
#         with open(f"./local/{lang_code}/info.json", "r", encoding="utf8") as info_file:
#             self.info.clear()
#             self.info = json.load(info_file)
#         with open(f"./local/{lang_code}/keyboards.json", "r", encoding="utf8") as keyboards_file:
#             self.keyboards.clear()
#             self.keyboards = json.load(keyboards_file)
#         with open(f"./local/{lang_code}/never_i_ever.json", "r", encoding="utf8") as never_i_ever_file:
#             self.never_i_ever.clear()
#             self.never_i_ever = json.load(never_i_ever_file)
#         with open(f"./local/{lang_code}/themes.json", "r", encoding="utf8") as themes_file:
#             self.themes.clear()
#             self.themes = json.load(themes_file)
#         with open(f"./local/{lang_code}/three_of_five.json", "r", encoding="utf8") as three_of_five_file:
#             self.three_of_five.clear()
#             self.three_of_five = json.load(three_of_five_file)
#         with open(f"./local/{lang_code}/truth_or_dare.json", "r", encoding="utf8") as truth_or_dare_file:
#             self.truth_or_dare.clear()
#             self.truth_or_dare = json.load(truth_or_dare_file)
#     @classmethod
#     def ensure_localisation(cls, user_lang_code):
#         if not self.lang_code:
#             self.load_localisation(user_lang_code)

class Texts:
    def __init__(self, lang_code):

        self.info = local.key_dicts.info
        self.keyboards = local.key_dicts.keyboards
        self.never_i_ever = local.key_dicts.never_i_ever
        self.themes = local.key_dicts.themes
        self.three_of_five = local.key_dicts.three_of_five
        self.truth_or_dare = local.key_dicts.truth_or_dare

        self.lang_code = lang_code

        self.load_localisation()


    def load_localisation(self):
        with open(f"./local/{self.lang_code}/info.json", "r", encoding="utf8") as info_file:
            self.info.clear()
            self.info = json.load(info_file)
        with open(f"./local/{self.lang_code}/keyboards.json", "r", encoding="utf8") as keyboards_file:
            self.keyboards.clear()
            self.keyboards = json.load(keyboards_file)
        with open(f"./local/{self.lang_code}/never_i_ever.json", "r", encoding="utf8") as never_i_ever_file:
            self.never_i_ever.clear()
            self.never_i_ever = json.load(never_i_ever_file)
        with open(f"./local/{self.lang_code}/themes.json", "r", encoding="utf8") as themes_file:
            self.themes.clear()
            self.themes = json.load(themes_file)
        with open(f"./local/{self.lang_code}/three_of_five.json", "r", encoding="utf8") as three_of_five_file:
            self.three_of_five.clear()
            self.three_of_five = json.load(three_of_five_file)
        with open(f"./local/{self.lang_code}/truth_or_dare.json", "r", encoding="utf8") as truth_or_dare_file:
            self.truth_or_dare.clear()
            self.truth_or_dare = json.load(truth_or_dare_file)

    def ensure_localisation(self):
        if not self.lang_code:
            self.load_localisation()
