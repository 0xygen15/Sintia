import logging

from aiogram import types
from aiogram.dispatcher import filters
from aiogram.types import Message

from mainUnit.config import admin_id, backup_channel_id, post_channel_id

from loader import dp, bot

from datetime import datetime

####

logging.basicConfig(level=logging.INFO)

####

"""Manual ads section. Admin sends ad to bot >>> bot sends ad to users from DB list"""

# photo_file_id = ""
# caption = ""
# @dp.message_handler(filters.IDFilter(chat_id=admin_id), commands="ads")
# async def ads_start(message: Message):
#     await AdsStates.reading.set()
#     await bot.send_message(chat_id=message.from_user.id, text="Send the post. Format: 1 photo + text with HTML formatting")
#
# @dp.message_handler(filters.IDFilter(chat_id=admin_id),state=AdsStates.reading, content_types=types.ContentType.ANY)
# async def ads_reading(message: Message):
#     global photo_file_id, caption
#     photo_file_id = message.photo[-1].file_id
#     caption = message.caption
#     await AdsStates.checking.set()
#     await bot.send_message(chat_id=message.from_user.id, text="This is what you gonna send to users:")
#     await bot.send_photo(chat_id=message.from_user.id, photo=photo_file_id, caption=caption, parse_mode="HTML")
#     await bot.send_message(chat_id=message.from_user.id, text="Confirm?")
#
# @dp.message_handler(filters.IDFilter(chat_id=admin_id),state=AdsStates.checking, content_types=types.ContentType.TEXT)
# async def ads_checking(message: Message, state: FSMContext):
#     global photo_file_id, caption
#     if message.text.lower() == 'yes':
#         for user_id in Users.chat_ids():
#             await bot.send_photo(chat_id=user_id, photo=photo_file_id, caption=caption, parse_mode="HTML")
#             await state.finish()
#     elif message.text.lower() == 'no':
#         photo_file_id = ""
#         caption = ""
#         await state.finish()


"""Forward ads section. Admin sends ad to channel >>> bot resends ad to bot """
@dp.channel_post_handler(filters.IDFilter(chat_id=post_channel_id), content_types=types.ContentType.ANY)
async def forward_from_channel(message: Message):
    for chat_id in Users.chat_ids():
        await bot.forward_message(chat_id=chat_id[0], from_chat_id=post_channel_id, message_id=message.message_id,
                                  disable_notification=False)

@dp.message_handler(filters.IDFilter(chat_id=admin_id), commands="backup_the_db")
async def backup_the_dp(message: Message):
    time = datetime.now()
    database_file = types.InputFile("../trash folder/users.db", f"users_{time}")
    file_caption = f"Back Up Time: {time}"
    await bot.send_document(chat_id=backup_channel_id, document=database_file, caption=file_caption)


@dp.message_handler(filters.IDFilter(chat_id=admin_id), commands="statistics")
async def statistics(message: Message):
    data = Users.get_statistics()
    await bot.send_message(chat_id=admin_id, text=data)


