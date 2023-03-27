import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, User

from mainUnit.states import AdsStates
from mainUnit.engine import Users
from mainUnit.token import admin_id

from loader import dp, bot

####

logging.basicConfig(level=logging.INFO)

photo_file_id = ""
caption = ""

####

"""Manual ads section. Admin sends ad to bot >>> bot sends ad to users from DB list"""
@dp.message_handler(commands="ads")
async def ads_start(message: Message):
    if message.from_user.id == admin_id:
        await AdsStates.reading.set()
        await bot.send_message(chat_id=message.from_user.id, text="Send the post. Format: 1 photo + text with HTML formatting")
    else:
        pass
@dp.message_handler(state=AdsStates.reading, content_types=types.ContentType.ANY)
async def ads_reading(message: Message):
    global photo_file_id, caption
    photo_file_id = message.photo[-1].file_id
    caption = message.caption
    await AdsStates.checking.set()
    await bot.send_message(chat_id=message.from_user.id, text="This is what you gonna send to users:")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_file_id, caption=caption, parse_mode="HTML")
    await bot.send_message(chat_id=message.from_user.id, text="Confirm?")

@dp.message_handler(state=AdsStates.checking, content_types=types.ContentType.TEXT)
async def ads_checking(message: Message, state: FSMContext):
    global photo_file_id, caption
    if message.text.lower() == 'yes':
        for user_id in Users.chat_ids():
            await bot.send_photo(chat_id=user_id, photo=photo_file_id, caption=caption, parse_mode="HTML")
            await state.finish()
    elif message.text.lower() == 'no':
        photo_file_id = ""
        caption = ""
        await state.finish()


"""Forward ads section. Admin sends ad to channel >>> bot resends ad to bot """
