from aiogram.types import Message, ContentTypes, CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from mainUnit.states import Feedback, Advertise
from mainUnit.config import feedback_channel_id

from mainUnit.users import loc_objects
from mainUnit.database import Database
from mainUnit.keyboards import TordKeyboard

tord_kb: TordKeyboard = TordKeyboard(loc_file=loc_objects["en"])


@dp.message_handler(commands='advertise', state='*')
async def advertise_pending(message: Message, state: FSMContext):
    # await state.finish()
    # await Advertise.pending.set()

    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)
    await dp.storage.set_state(chat=message.chat.id, user=message.from_user.id, state=Advertise.pending)

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb

    await bot.send_message(text=user_lang_code_object.info["advertise"], chat_id=message.from_user.id, parse_mode='HTML',
                           reply_markup=tord_kb.to_menu_kb)

@dp.callback_query_handler(tord_kb.to_menu_cb.filter(action=["main menu"]), state=Advertise.pending)
async def to_main_menu(query: CallbackQuery):
    await dp.storage.finish(chat=query.message.chat.id, user=query.from_user.id)
    user_obj = Database.retrieve_user_obj(query.from_user.id)
    user_lang_code_object = loc_objects[user_obj.lang_code]

    await bot.edit_message_text(text=user_lang_code_object.info["main_menu"], chat_id=query.from_user.id,
                                parse_mode='HTML',
                                message_id=query.message.message_id, reply_markup=None)

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
    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)