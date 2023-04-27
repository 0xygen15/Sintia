from typing import Dict, Any

from mainUnit.games import Tord, Nie, ThreeOfFive, Themes
from mainUnit.keyboards import TordKeyboard, NieKeyboard, ThreeOfFiveKeyboard, ThemesKeyboard
# from mainUnit.database import Database
from local.lang import Texts


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




#Localisation objects
loc_ru, loc_uk, loc_sr, loc_en, loc_de, loc_fr, loc_es = Texts("ru"), Texts("uk"), Texts("sr"), Texts("en"), Texts("de"), Texts("fr"), Texts("es")

#dict with user object where are all thew user's objects are stored
user_objects: Dict[str, Users|Any]= {}

#dict with loc objects for access from any place of project
loc_objects: Dict[str, Texts] = {
    "ru": loc_ru,
    "uk": loc_uk,
    "sr": loc_sr,
    "en": loc_en,
    "de": loc_de,
    "fr": loc_fr,
    "es": loc_es
}

def load_localisations():
    for loc_obj_code, loc_obj in loc_objects.items():
        loc_obj.load_localisation()

