import logging
import typing

from aiogram.types import CallbackQuery, Message

from mainUnit.engine import Engine
from mainUnit.keyboards import Keyboards
from mainUnit.players import Players


from loader import dp, bot

####

logging.basicConfig(level=logging.INFO)

engine = Engine()
player = Players()
keyboards = Keyboards()

data = []
message_id: int

####

@dp.message_handler(commands='three_of_five')
async def three_of_five_start(message: Message):
    global data
    data = engine.three_of_five()
    await bot.send_message(chat_id=message.from_user.id,
                           text="Описание игры (в разработке). Нажать кнопку для начала:",
                           reply_markup=keyboards.kb35)
    logging.info("Three of five game is on")


@dp.callback_query_handler(keyboards.cb35.filter(action=['Truth', 'Dare', 'Never', 'End']))
async def three_of_five_game(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    answer = callback_data['action']
    global data
    message_id = query.message.message_id
    match answer:
        case "Truth":
            text = data[0]
            await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                        reply_markup=keyboards.kb35, parse_mode='HTML')
        case "Dare":
            text = data[1]
            await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                        reply_markup=keyboards.kb35, parse_mode='HTML')
        case "Never":
            text = data[2]
            await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                        reply_markup=keyboards.kb35, parse_mode='HTML')
        case 'End':
            data = engine.three_of_five()
            text = "Чтобы начать новую игру нажми: /three_of_five"
            await bot.edit_message_text(text=text, chat_id=query.from_user.id, message_id=message_id,
                                        reply_markup=keyboards.kb35, parse_mode='HTML')


