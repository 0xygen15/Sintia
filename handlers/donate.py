from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from mainUnit.config import donation_links

from mainUnit.users import loc_objects
from mainUnit.database import Database
from mainUnit.keyboards import TordKeyboard


tord_kb: TordKeyboard = TordKeyboard(loc_file=loc_objects["en"])

@dp.message_handler(commands='donate', state='*')
async def donate(message: Message, state: FSMContext):
    # await state.finish()
    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb

    text = user_lang_code_object.info["donate"] + "\n\n" + donation_links
    await bot.send_message(text=text, chat_id=message.from_user.id, parse_mode='HTML',
                           reply_markup=tord_kb.to_menu_kb)


@dp.callback_query_handler(tord_kb.to_menu_cb.filter(action=["main menu"]))
async def to_main_menu(query: CallbackQuery):
    user_obj = Database.retrieve_user_obj(query.from_user.id)
    user_lang_code_object = loc_objects[user_obj.lang_code]

    await bot.edit_message_text(text=user_lang_code_object.info["main_menu"], chat_id=query.from_user.id,
                                parse_mode='HTML',
                                message_id=query.message.message_id, reply_markup=None)