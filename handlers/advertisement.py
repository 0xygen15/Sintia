import typing

from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from mainUnit.states import Feedback, Advertise
from mainUnit.config import feedback_channel_id

from local.lang import Texts


@dp.message_handler(commands='advertise', state='*')
async def advertise_pending(message: Message, state: FSMContext):
    await state.finish()
    await Advertise.pending.set()
    await bot.send_message(text=Texts.info["advertise"], chat_id=message.from_user.id, parse_mode='HTML')

@dp.message_handler(state=Feedback.pending, content_types=ContentTypes.ANY)
async def advertise_submit(message: Message, state: FSMContext):
    message_text = message.text
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    text = f"ADVERTISEMENT REQUEST\n\nНовое сообщение от @{user_name}\n\n'''{message_text}'''\n\n{first_name} | {last_name}\nid:{user_id}"
    await bot.send_message(text=text, chat_id=feedback_channel_id, parse_mode='HTML')
    await bot.send_message(text='☑️☑️☑️', chat_id=message.from_user.id, parse_mode='HTML')
    await state.finish()