from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from mainUnit.states import Feedback
from mainUnit.config import feedback_channel_id

from mainUnit.users import loc_objects
from mainUnit.database import Database

from local.lang import Texts

@dp.message_handler(commands='feedback', state='*')
async def feedback_pending(message: Message, state: FSMContext):
    # await state.finish()
    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)
    await dp.storage.set_state(chat=message.chat.id, user=message.from_user.id, state=Feedback.pending)
    # await Feedback.pending.set()

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    user_lang_code_object = loc_objects[user_obj.lang_code]

    await bot.send_message(text=user_lang_code_object.info["feedback"], chat_id=message.from_user.id, parse_mode='HTML')

@dp.message_handler(state=Feedback.pending, content_types=ContentTypes.ANY)
async def feedback_submit(message: Message, state: FSMContext):

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    user_lang_code_object = loc_objects[user_obj.lang_code]

    message_text = message.text
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    text = f"FEEDBACK\n\nНовое сообщение от @{user_name}\n\n'''{message_text}'''\n\n{first_name} | {last_name}\nid:{user_id}"
    await bot.send_message(text=text, chat_id=feedback_channel_id, parse_mode='HTML')

    await bot.send_message(text='Thank you for your feedback', chat_id=message.from_user.id, parse_mode='HTML')
    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)