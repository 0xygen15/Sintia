from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from mainUnit.users import loc_objects

from mainUnit.users import Users
from mainUnit.games import Tord, Nie, ThreeOfFive, Themes
from mainUnit.keyboards import TordKeyboard, NieKeyboard, ThemesKeyboard, ThreeOfFiveKeyboard
from mainUnit.database import Database

@dp.message_handler(commands='info')
async def info(message: Message):
    user_obj = Database.retrieve_user_obj(message.from_user.id)
    await bot.send_message(text=loc_objects[user_obj.lang_code].info["info"], chat_id=message.from_user.id, parse_mode='HTML')


@dp.message_handler(commands=['start', 'main_menu'])
async def start(message: Message):
    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)
    try:
        user_obj = Database.retrieve_user_obj(message.from_user.id)
        # lang_code = user_obj.lang_code
    except:
        lang_code = message.from_user.language_code

        user = Users(
            user_id=message.from_user.id,
            lang_code=lang_code,
            tord_game=Tord(message.from_user.id, lang_code),
            nie_game=Nie(message.from_user.id, lang_code),
            the_35_game=ThreeOfFive(message.from_user.id, lang_code),
            themes_game=Themes(message.from_user.id, lang_code),
            tord_kb=TordKeyboard(loc_objects[lang_code]),
            nie_kb=NieKeyboard(loc_objects[lang_code]),
            the_35_kb=ThreeOfFiveKeyboard(loc_objects[lang_code]),
            themes_kb=ThemesKeyboard(loc_objects[lang_code]),
            chat_id=message.chat.id,
            chat_type=message.chat.type,
            username=message.from_user.username,
            fName=message.from_user.first_name,
            lName=message.from_user.last_name,
            is_bot=message.from_user.is_bot
        )

        Database.create_users_table() # create db if not created
        Database.add_user_to_db(user) #add user data to db if bot added yet

        user_obj = Database.retrieve_user_obj(message.from_user.id)

    user_lang_code_object = loc_objects[user_obj.lang_code]

    await bot.send_message(text=user_lang_code_object.info["main_menu"], chat_id=message.from_user.id, parse_mode='HTML')

# @dp.message_handler(commands='main_menu', state='*')
# async def main_menu(message: Message):
#     await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)
#
#     user_obj = Database.retrieve_user_obj(message.from_user.id)
#     user_lang_code_object = loc_objects[user_obj.lang_code]
#
#     await bot.send_message(text=user_lang_code_object.info["main_menu"], chat_id=message.from_user.id, parse_mode='HTML')
