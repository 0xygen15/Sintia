import logging
import typing

from aiogram.types import CallbackQuery, Message

from mainUnit.engine import Engine
from mainUnit.keyboards import Keyboards, ThemesKeyboard
from mainUnit.players import Players
from handlers.info import *

from local.lang import Texts

from loader import dp, bot

####

logging.basicConfig(level=logging.INFO)

engine = Engine()
player = Players()
# keyboards = Keyboards()
keyboards = ThemesKeyboard()

theme_chosen: str
data = []
index: int

# texts = Texts.themes
####

@dp.message_handler(commands='themes')
async def themes_start(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=Texts.themes["make choice"],
                           reply_markup=keyboards.kb_themes)


@dp.callback_query_handler(keyboards.cb_themes.filter(action=["school",
                                                              "work",
                                                              "travel",
                                                              "worldview",
                                                              "social media",
                                                              "art",
                                                              "relations",
                                                              "memes",
                                                              "religion",
                                                              "memories",
                                                              "if",
                                                              "videogames",
                                                              "education",
                                                              "fashion",
                                                              "hard choice"]))
async def themes_choice(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    answer = callback_data['action']
    global theme_chosen
    message_id = query.message.message_id
    theme_chosen = answer
    key = answer+" name"
    await bot.edit_message_text(text=f"{Texts.themes[key]}", chat_id=query.from_user.id, message_id=message_id,
                                        reply_markup=keyboards.kb_themes_confirm, parse_mode='HTML')


@dp.callback_query_handler(keyboards.cb_themes_confirm.filter(action=["menu", "begin"]))
async def themes_confirm(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    answer = callback_data['action']
    global theme_chosen, data, index
    message_id = query.message.message_id
    if answer == "menu":
        theme_chosen = ""
        await bot.edit_message_text(text=Texts.themes["make choice"],
                                    chat_id=query.from_user.id,
                                    message_id=message_id,
                                    reply_markup=keyboards.kb_themes,
                                    parse_mode='HTML')
    elif answer == "begin":
        data = engine.theme(theme_chosen)
        index = 0
        current_question = data[index]
        await bot.edit_message_text(text=f"{current_question}",
                                    chat_id=query.from_user.id,
                                    message_id=message_id,
                                    reply_markup=keyboards.kb_themes_game,
                                    parse_mode='HTML')

@dp.callback_query_handler(keyboards.cb_themes_game.filter(action=["next", "previous", "end"]))
async def themes_game(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    answer = callback_data['action']
    message_id = query.message.message_id
    global theme_chosen, data, index
    if answer == "next":
        if index > len(data)-1:
            theme_chosen = ""
            await bot.edit_message_text(text=Texts.themes["game over"],
                                        chat_id=query.from_user.id,
                                        message_id=message_id,
                                        reply_markup=keyboards.kb_themes,
                                        parse_mode='HTML')
        else:
            index += 1
            current_question = data[index]
            await bot.edit_message_text(text=f"{current_question}",
                                        chat_id=query.from_user.id,
                                        message_id=message_id,
                                        reply_markup=keyboards.kb_themes_game,
                                        parse_mode='HTML')
    elif answer == "previous":
        if index == 0:
            index = 0
            pass

        else:
            index -= 1
            current_question = data[index]
            await bot.edit_message_text(text=f"{current_question}",
                                        chat_id=query.from_user.id,
                                        message_id=message_id,
                                        reply_markup=keyboards.kb_themes_game,
                                        parse_mode='HTML')
    elif answer == "end":
        theme_chosen = ""
        await bot.edit_message_text(text=Texts.themes["game over"],
                                    chat_id=query.from_user.id,
                                    message_id=message_id,
                                    reply_markup=keyboards.kb_themes,
                                    parse_mode='HTML')