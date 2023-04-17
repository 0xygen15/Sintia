import logging
import typing

from aiogram.types import CallbackQuery, Message

from mainUnit.engine import Engine
from mainUnit.keyboards import Keyboards, ThreeOfFiveKeyboard
from mainUnit.players import Players

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

####

@dp.message_handler(commands='three_of_five')
async def three_of_five_start(message: Message):
    global data
    data = engine.three_of_five()
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
                                    reply_markup=keyboards.kb35, parse_mode='HTML')


