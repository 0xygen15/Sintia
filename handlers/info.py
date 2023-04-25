from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from loader import loc_objects, user_objects

from mainUnit.users import Users
from mainUnit.games import Tord, Nie, ThreeOfFive, Themes
from mainUnit.keyboards import TordKeyboard, NieKeyboard, ThemesKeyboard, ThreeOfFiveKeyboard
from mainUnit.database import Database

@dp.message_handler(commands='info')
async def info(message: Message):
    user_obj = Users.retrieve_user_obj(message.from_user.id)
    await bot.send_message(text=loc_objects[user_obj.lang_code].info["info"], chat_id=message.from_user.id, parse_mode='HTML')


@dp.message_handler(commands='start')
async def start(message: Message, state: FSMContext):
    await state.finish()
    user = Users(
        user_id=message.from_user.id,
        lang_code=message.from_user.language_code,
        tord_game=Tord(message.from_user.id, message.from_user.language_code),
        nie_game=Nie(message.from_user.id, message.from_user.language_code),
        the_35_game=ThreeOfFive(message.from_user.id, message.from_user.language_code),
        themes_game=Themes(message.from_user.id, message.from_user.language_code),
        tord_kb=TordKeyboard(message.from_user.language_code),
        nie_kb=NieKeyboard(message.from_user.language_code),
        the_35_kb=ThreeOfFiveKeyboard(message.from_user.language_code),
        themes_kb=ThemesKeyboard(message.from_user.language_code),
        chat_id=message.chat.id,
        chat_type=message.chat.type,
        username=message.from_user.username,
        fName=message.from_user.first_name,
        lName=message.from_user.last_name,
        is_bot=message.from_user.is_bot
    )

    Database.create_users_db() # create db if not created
    Database.add_user_to_db(user) #add user data to db if bot added yet

    user_obj = Users.retrieve_user_obj(message.from_user.id)

    user_lang_code_object = loc_objects[user_objects[message.from_user.id].lang_code]
    user_lang_code_object.load_localisation() #load localisation files

    await bot.send_message(text=user_lang_code_object.info["start"], chat_id=message.from_user.id, parse_mode='HTML')

@dp.message_handler(commands='main_menu', state='*')
async def main_menu(message: Message, state: FSMContext):
    await state.finish()
    user_obj = Users.retrieve_user_obj(message.from_user.id)
    user_lang_code_object = loc_objects[user_obj.lang_code]
    user_lang_code_object.load_localisation()
    await bot.send_message(text=loc_objects[user_objects[message.from_user.id].lang_code].info["main_menu"], chat_id=message.from_user.id, parse_mode='HTML')
