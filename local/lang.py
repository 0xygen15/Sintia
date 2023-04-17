import json
import local.key_dicts
class Texts:

    info = local.key_dicts.info
    keyboards = local.key_dicts.keyboards
    never_i_ever = local.key_dicts.never_i_ever
    themes = local.key_dicts.themes
    three_of_five = local.key_dicts.three_of_five
    truth_or_dare = local.key_dicts.truth_or_dare

    # info = {}
    # keyboards = {}
    # never_i_ever = {}
    # themes = {}
    # three_of_five = {}
    # truth_or_dare = {}

    handlers_list = [
        ["info.json", info],
        ["keyboards.json", keyboards],
        ["never_i_ever.json", never_i_ever],
        ["themes.json", themes],
        ["three_of_five.json", three_of_five],
        ["truth_or_dare.json", truth_or_dare]]

    lang_code = ""

    lang_codes = ["en", "de", "es", "fr", "uk", "sr"]
    @classmethod
    def load_localisation(cls, lang_code):
        # for handler_item in cls.handlers_list:
        #     with open(f"./local/{lang_code}/{handler_item[0]}", "r", encoding="utf8") as file:
        #         handler_item[1] = {}
        #         handler_item[1] = json.load(file)
        with open(f"./local/{lang_code}/info.json", "r", encoding="utf8") as info_file:
            cls.info.clear()
            cls.info = json.load(info_file)
        with open(f"./local/{lang_code}/keyboards.json", "r", encoding="utf8") as keyboards_file:
            cls.keyboards.clear()
            cls.keyboards = json.load(keyboards_file)
        with open(f"./local/{lang_code}/never_i_ever.json", "r", encoding="utf8") as never_i_ever_file:
            cls.never_i_ever.clear()
            cls.never_i_ever = json.load(never_i_ever_file)
        with open(f"./local/{lang_code}/themes.json", "r", encoding="utf8") as themes_file:
            cls.themes.clear()
            cls.themes = json.load(themes_file)
        with open(f"./local/{lang_code}/three_of_five.json", "r", encoding="utf8") as three_of_five_file:
            cls.three_of_five.clear()
            cls.three_of_five = json.load(three_of_five_file)
        with open(f"./local/{lang_code}/truth_or_dare.json", "r", encoding="utf8") as truth_or_dare_file:
            cls.truth_or_dare.clear()
            cls.truth_or_dare = json.load(truth_or_dare_file)
    @classmethod
    def ensure_localisation(cls, user_lang_code):
        if not cls.lang_code:
            cls.load_localisation(user_lang_code)