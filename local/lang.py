import json

class Texts:
    texts = {}
    @classmethod
    def load_localisation(cls, lang_code):
        with open(f"../local/{lang_code}.json", "r", encoding="utf8") as file:
            cls.texts = json.load(file)
    @classmethod
    def ensure_localisation(cls, user_lang_code):
        if bool(cls.texts) == False or cls.texts["lang_code"] != user_lang_code:
            cls.load_localisation(user_lang_code)
