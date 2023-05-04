import logging
import typing

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from mainUnit.engine import Engine
from mainUnit.keyboards import ThreeOfFiveKeyboard
from mainUnit import Players

from local.lang import Texts

from loader import dp, bot

####

logging.basicConfig(level=logging.INFO)

engine = Engine()
player = Players()
# keyboards = Keyboards()
keyboards = ThreeOfFiveKeyboard()

data = []

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

@dp.message_handler(commands='three_of_five', state='*')
async def three_of_five_start(message: Message, state: FSMContext):
    global keyboards, engine, player
    await state.finish()
    global data
    data = engine.three_of_five()
    # keyboards, engine, player = update_keyboards_object()
    keyboards, engine, player = ThreeOfFiveKeyboard(), Engine(), Players()
    await bot.send_message(chat_id=message.from_user.id,
                           text=Texts.three_of_five["description"],
                           reply_markup=keyboards.kb35)
    logging.info("Three of five game is on")


@dp.callback_query_handler(keyboards.cb35.filter(action=['Truth', 'Dare', 'Never', 'End']))
async def three_of_five_game(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    answer = callback_data['action']
    global data
    message_id = query.message.message_id
    if answer == "Truth":
        text = data[0]
        await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                    reply_markup=keyboards.kb35, parse_mode='HTML')
    elif answer == "Dare":
        text = data[1]
        await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                    reply_markup=keyboards.kb35, parse_mode='HTML')
    elif answer == "Never":
        text = data[2]
        await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                    reply_markup=keyboards.kb35, parse_mode='HTML')
    elif answer == 'End':
        data = engine.three_of_five()
        text = f"{Texts.three_of_five['new game']} /three_of_five"
        await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                    parse_mode='HTML')
        await bot.send_message(text=Texts.info["main_menu"], chat_id=query.from_user.id, parse_mode='HTML')

