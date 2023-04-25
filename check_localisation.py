from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from loader import loc_objects, user_objects

from mainUnit.users import Users
from mainUnit.games import Tord, Nie, ThreeOfFive, Themes
from mainUnit.keyboards import TordKeyboard, NieKeyboard, ThemesKeyboard, ThreeOfFiveKeyboard
from mainUnit.database import Database

test_user = Users(
    user_id="107985053",
    lang_code="ru",
    tord_game=Tord("107985053", loc_objects["ru"]),
    nie_game=Nie("107985053", loc_objects["ru"]),
    the_35_game=ThreeOfFive("107985053", loc_objects["ru"]),
    themes_game=Themes("107985053", loc_objects["ru"]),
    tord_kb=TordKeyboard(loc_objects["ru"]),
    nie_kb=NieKeyboard(loc_objects["ru"]),
    the_35_kb=ThreeOfFiveKeyboard(loc_objects["ru"]),
    themes_kb=ThemesKeyboard(loc_objects["ru"]),
    chat_id="107985053",
    chat_type="user",
    username="test_username",
    fName="test fName",
    lName="test lName",
    is_bot=False
)

user_objects['test'] = test_user

user_lang_code_object = loc_objects[user_objects['test'].lang_code]
user_lang_code_object.load_localisation()  # load localisation files

print(user_lang_code_object.info)