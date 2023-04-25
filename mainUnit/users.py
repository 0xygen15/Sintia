from mainUnit.games import Tord, Nie, ThreeOfFive, Themes
from mainUnit.keyboards import TordKeyboard, NieKeyboard, ThreeOfFiveKeyboard, ThemesKeyboard
from mainUnit.database import Database

from loader import user_objects

class Users:
    def __init__(self, user_id: str | int, lang_code: str,
                 tord_game: Tord, nie_game: Nie,
                 the_35_game: ThreeOfFive, themes_game: Themes,
                 tord_kb: TordKeyboard, nie_kb: NieKeyboard,
                 the_35_kb: ThreeOfFiveKeyboard, themes_kb: ThemesKeyboard,
                 chat_id: str | int, chat_type: str,
                 username: str, fName: str, lName: str,
                 is_bot: bool):

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

        self.chat_id = chat_id
        self.chat_type = chat_type
        self.username = username
        self.fName = fName
        self.lName = lName
        self.is_bot = is_bot

    @classmethod
    def retrieve_user_obj(cls, user_id):
        try:
            user_obj = user_objects[user_id]
        except KeyError:
            user_objects[user_id] = Database.get_user_obj_from_db(user_id)
            user_obj = user_objects[user_id]

        return user_obj
