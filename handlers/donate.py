import typing

from aiogram.types import Message, CallbackQuery, ContentTypes
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from mainUnit.engine import Users
from mainUnit.keyboards import ConfigKeyboard
from mainUnit.states import LangStates, Feedback, Advertise
from mainUnit.config import admin_id, feedback_channel_id, post_channel_id, donation_links

from local.lang import Texts

@dp.message_handler(commands='donate', state='*')
async def donate(message: Message, state: FSMContext):
    await state.finish()
    text = Texts.info["donate"] + "\n\n" + donation_links
    await bot.send_message(text=text, chat_id=message.from_user.id, parse_mode='HTML')