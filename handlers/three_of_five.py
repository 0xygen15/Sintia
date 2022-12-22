import logging
import typing

from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from mainUnit.engine import Engine
from mainUnit.keyboards import Keyboards
from mainUnit.players import Players
from mainUnit.states import PlayerStates


from loader import dp, bot

####

logging.basicConfig(level=logging.INFO)

engine = Engine()
player = Players()
keyboards = Keyboards()


def one_part(all, part):
    q = ""
    for k, v in all[part].items():
        q += v
        q += "\n"
    return q

####

@dp.message_handler(commands='three_of_five')
async def players_names(message: Message):
    all = engine.three_of_five()


    await bot.send_message(chat_id=message.from_user.id,
                           text="")
    logging.info("Three of five game is on")