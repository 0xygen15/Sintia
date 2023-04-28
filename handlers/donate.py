import typing

from aiogram.types import Message, CallbackQuery, ContentTypes
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from mainUnit.engine import Users
from mainUnit.keyboards import ConfigKeyboard
from mainUnit.states import LangStates, Feedback, Advertise
from mainUnit.config import admin_id, feedback_channel_id, post_channel_id, donation_links

from mainUnit.users import loc_objects
from mainUnit.database import Database

from local.lang import Texts

@dp.message_handler(commands='donate', state='*')
async def donate(message: Message, state: FSMContext):
    # await state.finish()
    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    user_lang_code_object = loc_objects[user_obj.lang_code]

    text = user_lang_code_object.info["donate"] + "\n\n" + donation_links
    await bot.send_message(text=text, chat_id=message.from_user.id, parse_mode='HTML')