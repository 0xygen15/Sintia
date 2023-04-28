import logging
import typing

from aiogram.types import CallbackQuery, Message

from mainUnit.states import ThreeOfFiveStates
from mainUnit.users import loc_objects
from mainUnit.keyboards import ThreeOfFiveKeyboard
from mainUnit.database import Database

from loader import dp, bot

####

logging.basicConfig(level=logging.INFO)

# engine = Engine()
# player = Players()
# keyboards = Keyboards()
# keyboards = ThreeOfFiveKeyboard()

# data = []

# texts = Texts.three_of_five

# def update_keyboards_object():
#     global keyboards, engine, player
#     if Texts.lang_code:
#         keyboards_en = ThreeOfFiveKeyboard()
#         keyboards = keyboards_en
#         engine_updated = Engine()
#         engine = engine_updated
#         player_updated = Players()
#         player = player_updated
#         return keyboards, engine, player

####
the35_kb: ThreeOfFiveKeyboard = ThreeOfFiveKeyboard(loc_file=loc_objects['en'])


@dp.message_handler(commands='three_of_five', state='*')
async def three_of_five_start(message: Message):
    # global keyboards, engine, player
    # await state.finish()
    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)
    # global data

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    the35_game_obj = user_obj.the_35_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    the35_kb = user_obj.the_35_game

    # data = engine.three_of_five()
    # keyboards, engine, player = update_keyboards_object()
    # keyboards, engine, player = ThreeOfFiveKeyboard(), Engine(), Players()
    await bot.send_message(chat_id=message.from_user.id,
                           text=user_lang_code_object.three_of_five["description"],
                           reply_markup=the35_kb.kb35)
    logging.info("Three of five game is on")


@dp.callback_query_handler(the35_kb.cb35.filter(action=['Truth', 'Dare', 'Never', 'End']))
async def three_of_five_game(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    answer = callback_data['action']
    # global data

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    the35_game_obj = user_obj.the_35_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    the35_kb = user_obj.the_35_game

    message_id = query.message.message_id
    if answer == "Truth":
        text = the35_game_obj.truths_str
        await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                    reply_markup=the35_kb.kb35, parse_mode='HTML')
    elif answer == "Dare":
        text = the35_game_obj.dares_str
        await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                    reply_markup=the35_kb.kb35, parse_mode='HTML')
    elif answer == "Never":
        text = the35_game_obj.nevers_str
        await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                    reply_markup=the35_kb.kb35, parse_mode='HTML')
    elif answer == 'End':
        the35_game_obj.reset()
        text = f"{user_lang_code_object.three_of_five['new game']} /three_of_five"
        await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                    parse_mode='HTML')
        await bot.send_message(text=user_lang_code_object.info["main_menu"], chat_id=query.from_user.id, parse_mode='HTML')


