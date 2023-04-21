user_objects = {}

class Users:
    def __init__(self, user_id, lang_code, tord_game, nie_game, the_35_game, themes_game, tord_kb, nie_kb, the_35_kb, themes_kb):

        self.user_id = user_id
        self.lang_code = lang_code

        self.tord_game = tord_game
        self.nie_game = nie_game
        self.the_35_game = the_35_game
        self.themes_game = themes_game

        self.tord_kb = tord_kb
        self.nie_kb = nie_kb
        self.the_35_kb = the_35_kb
        self.themes_kb = themes_kb