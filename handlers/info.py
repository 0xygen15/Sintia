import typing

from aiogram.types import Message, CallbackQuery, ContentTypes
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from mainUnit.engine import Users
from mainUnit.keyboards import ConfigKeyboard
from mainUnit.states import LangStates, Feedback, Advertise
from mainUnit.config import admin_id, feedback_channel_id, post_channel_id

from local.lang import Texts

@dp.message_handler(commands='info')
async def info(message: Message):
    await bot.send_message(text=Texts.info["info"], chat_id=message.from_user.id, parse_mode='HTML')


@dp.message_handler(commands='start')
async def start(message: Message, state: FSMContext):
    await state.finish()
    user_chat_data = {
        'chat_id': message.chat.id,
        'chat_type': message.chat.type,
        'username': message.from_user.username,
        'fName': message.from_user.first_name,
        'lName': message.from_user.last_name,
        'user_id': message.from_user.id,
        'language_code': message.from_user.language_code,
        'is_bot': message.from_user.is_bot
    }
    Users.create_table() # create db if not created
    Users.create(user_chat_data) #add user data to db if bot added yet
    Texts.lang_code = Users.get_user_lang_code(message.from_user.id)
    Texts.load_localisation(Texts.lang_code) #load localisation files
    await bot.send_message(text=Texts.info["start"], chat_id=message.from_user.id, parse_mode='HTML')

@dp.message_handler(commands='main_menu', state='*')
async def main_menu(message: Message, state: FSMContext):
    await state.finish()
    Texts.ensure_localisation(Texts.lang_code)
    await bot.send_message(text=Texts.info["main_menu"], chat_id=message.from_user.id, parse_mode='HTML')


# @dp.message_handler(commands='refresh', state='*')
# async def start(message: Message, state: FSMContext):
#     await state.finish()
#     await bot.send_message(text=Texts.info["refresh"], chat_id=message.from_user.id, parse_mode='HTML')