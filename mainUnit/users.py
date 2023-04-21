user_objects = {}

class Users:
    def __init__(self, user_id, lang_code, engine, keyboards, players):
        self.user_id = user_id
        self.lang_code = lang_code
        self.engine = engine
        self.keyboards = keyboards
        self.players = players