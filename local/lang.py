import json
import local.key_dicts
class Texts:

    info = local.key_dicts.info
    keyboards = local.key_dicts.keyboards
    never_i_ever = local.key_dicts.never_i_ever
    themes = local.key_dicts.themes
    three_of_five = local.key_dicts.three_of_five
    truth_or_dare = local.key_dicts.truth_or_dare

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
        for handler_item in cls.handlers_list:
            with open(f"../local/{lang_code}/{handler_item[0]}", "r", encoding="utf8") as file:
                handler_item[1] = json.load(file)
    @classmethod
    def ensure_localisation(cls, user_lang_code):
        for handler_item in cls.handlers_list:
            if not bool(handler_item[1]):
                cls.load_localisation(user_lang_code)
