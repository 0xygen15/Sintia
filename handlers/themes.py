import logging
import typing

from aiogram.types import CallbackQuery, Message

from mainUnit.engine import Engine
from mainUnit.keyboards import ThemesKeyboard
from mainUnit.players import Players
from mainUnit.states import ThemesStates
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

def keyboard_local():
    global keyboards
    if Texts.lang_code == "en":
        keyboards_en = ThemesKeyboard()
        keyboards = keyboards_en
        return keyboards
    elif Texts.lang_code == "de":
        keyboards_de = ThemesKeyboard()
        keyboards = keyboards_de
        return keyboards
    elif Texts.lang_code == "fr":
        keyboards_fr = ThemesKeyboard()
        keyboards = keyboards_fr
        return keyboards
    elif Texts.lang_code == "es":
        keyboards_es = ThemesKeyboard()
        keyboards = keyboards_es
        return keyboards
    elif Texts.lang_code == "ru":
        keyboards_ru = ThemesKeyboard()
        keyboards = keyboards_ru
        return keyboards
    elif Texts.lang_code == "uk":
        keyboards_uk = ThemesKeyboard()
        keyboards = keyboards_uk
        return keyboards
    elif Texts.lang_code == "sr":
        keyboards_sr = ThemesKeyboard()
        keyboards = keyboards_sr
        return keyboards
    else:
        keyboards_en = ThemesKeyboard()
        keyboards = keyboards_en
        return keyboards

# texts = Texts.themes
####

@dp.message_handler(commands='themes')
async def themes_start(message: Message, state: FSMContext):
    global keyboards
    await state.finish()
    await ThemesStates.theme_choice.set()
    keyboards = keyboard_local()
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
                                                              "hard choice"]),
                           state=ThemesStates.theme_choice)
async def themes_choice(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    await ThemesStates.confirmation.set()
    global theme_chosen

    answer = callback_data['action']
    message_id = query.message.message_id
    theme_chosen = answer
    key = answer+" name"

    await bot.edit_message_text(text=f"{Texts.themes[key]}", chat_id=query.from_user.id, message_id=message_id,
                                        reply_markup=keyboards.kb_themes_confirm, parse_mode='HTML')


@dp.callback_query_handler(keyboards.cb_themes_confirm.filter(action=["menu", "begin"]), state=ThemesStates.confirmation.set())
async def themes_confirm(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    global theme_chosen, data, index

    answer = callback_data['action']
    message_id = query.message.message_id

    if answer == "menu":
        await ThemesStates.theme_choice.set()
        theme_chosen = ""
        await bot.edit_message_text(text=Texts.themes["make choice"],
                                    chat_id=query.from_user.id,
                                    message_id=message_id,
                                    reply_markup=keyboards.kb_themes,
                                    parse_mode='HTML')
    elif answer == "begin":
        await ThemesStates.game.set()
        data = engine.theme(theme_chosen)
        index = 0
        current_question = data[index]
        await bot.edit_message_text(text=f"{current_question}",
                                    chat_id=query.from_user.id,
                                    message_id=message_id,
                                    reply_markup=keyboards.kb_themes_game,
                                    parse_mode='HTML')

@dp.callback_query_handler(keyboards.cb_themes_game.filter(action=["next", "previous", "end"]), state=ThemesStates.game)
async def themes_game(query: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):
    global theme_chosen, data, index

    answer = callback_data['action']
    message_id = query.message.message_id

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
        await state.finish()
        theme_chosen = ""
        await bot.edit_message_text(text=Texts.themes["game over"],
                                    chat_id=query.from_user.id,
                                    message_id=message_id,
                                    reply_markup=keyboards.kb_themes,
                                    parse_mode='HTML')