import logging
import typing

import aiogram.types
from aiogram.types import CallbackQuery, Message

from mainUnit.states import ThreeOfFiveStates
from mainUnit.users import loc_objects
from mainUnit.keyboards import ThreeOfFiveKeyboard
from mainUnit.database import Database

from loader import dp, bot

####

logging.basicConfig(level=logging.INFO)

the35_kb: ThreeOfFiveKeyboard = ThreeOfFiveKeyboard(loc_file=loc_objects['en'])


@dp.message_handler(commands='three_of_five', state='*')
async def three_of_five_start(message: Message):
    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    the35_game_obj = user_obj.the_35_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    the35_kb = user_obj.the_35_kb

    await bot.send_message(chat_id=message.from_user.id,
                           text=user_lang_code_object.three_of_five["description"],
                           reply_markup=the35_kb.kb35b)
    logging.info("Three of five game is on")


# @dp.callback_query_handler(the35_kb.cb35.filter(action=['Truth', 'Dare', 'Never', 'End']))
# async def three_of_five_game(query: CallbackQuery, callback_data: typing.Dict[str, str]):
#     answer = callback_data['action']
#
#     user_obj = Database.retrieve_user_obj(query.from_user.id)
#     the35_game_obj = user_obj.the_35_game
#     user_lang_code_object = loc_objects[user_obj.lang_code]
#     the35_kb = user_obj.the_35_kb
#
#     message_id = query.message.message_id
#     if answer == "Truth":
#         text = the35_game_obj.truths_str
#         await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
#                                     reply_markup=the35_kb.kb35, parse_mode='HTML')
#     elif answer == "Dare":
#         text = the35_game_obj.dares_str
#         await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
#                                     reply_markup=the35_kb.kb35, parse_mode='HTML')
#     elif answer == "Never":
#         text = the35_game_obj.nevers_str
#         await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
#                                     reply_markup=the35_kb.kb35, parse_mode='HTML')
#     elif answer == 'End':
#         the35_game_obj.reset()
#         text = f"{user_lang_code_object.three_of_five['new game']} /three_of_five"
#         await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
#                                     parse_mode='HTML', reply_markup=None)
#         await bot.send_message(text=user_lang_code_object.info["main_menu"], chat_id=query.from_user.id, parse_mode='HTML')

@dp.callback_query_handler(the35_kb.cb35b.filter(action=["begin", "main menu"]))
async def three_of_five_setup(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    answer = callback_data['action']

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    the35_game_obj = user_obj.the_35_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    the35_kb = user_obj.the_35_kb

    message_id = query.message.message_id
    if answer == "main menu":
        await bot.edit_message_text(text=user_lang_code_object.info["main_menu"], chat_id=query.from_user.id,
                                    message_id=message_id, reply_markup=None, parse_mode='HTML')
    elif answer == "begin":
        the35_game_obj.main_func()
        the35_game_obj.index = 0

        text = f"<b>{the35_game_obj.index + 1}/15</b>\n\n{the35_game_obj.game_list[the35_game_obj.index]}"

        await bot.edit_message_text(text=text, chat_id=query.from_user.id,
                                    message_id=message_id, reply_markup=the35_kb.kb35n, parse_mode='HTML')


@dp.callback_query_handler(the35_kb.cb35n.filter(action=['previous', 'next', 'end']))
async def three_of_five_game(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    answer = callback_data['action']

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    the35_game_obj = user_obj.the_35_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    the35_kb = user_obj.the_35_kb

    message_id = query.message.message_id

    if answer == "previous":
        if the35_game_obj.index <= 0:
            pass
        else:
            the35_game_obj.index -= 1
            text = f"<b>{the35_game_obj.index + 1}/15</b>\n\n{the35_game_obj.game_list[the35_game_obj.index]}"
            await bot.edit_message_text(text=text, chat_id=query.from_user.id,
                                        message_id=message_id, reply_markup=the35_kb.kb35n, parse_mode='HTML')
    elif answer == "next":
        if the35_game_obj.index >= len(the35_game_obj.game_list) - 1:
            pass
        else:
            the35_game_obj.index += 1
            text = f"<b>{the35_game_obj.index + 1}/15</b>\n\n{the35_game_obj.game_list[the35_game_obj.index]}"
            await bot.edit_message_text(text=text, chat_id=query.from_user.id,
                                        message_id=message_id, reply_markup=the35_kb.kb35n, parse_mode='HTML')
    elif answer == "end":
        the35_game_obj.reset()
        # text = f"{user_lang_code_object.three_of_five['new game']} /three_of_five"
        # await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
        #                             parse_mode='HTML', reply_markup=None)
        await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
        await bot.send_message(text=user_lang_code_object.info["main_menu"], chat_id=query.from_user.id,
                               parse_mode='HTML')



