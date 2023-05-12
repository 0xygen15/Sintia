import logging
import typing

from aiogram.types import CallbackQuery, Message

from mainUnit.states import ThemesStates
from mainUnit.users import loc_objects
from mainUnit.keyboards import ThemesKeyboard
from mainUnit.database import Database

from loader import dp, bot

####

logging.basicConfig(level=logging.INFO)
####

themes_kb: ThemesKeyboard = ThemesKeyboard(loc_file=loc_objects['en'])

@dp.message_handler(commands='themes', state='*')
async def themes_start(message: Message):
    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)
    await dp.storage.set_state(chat=message.chat.id, user=message.from_user.id, state=ThemesStates.theme_choice)

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    themes_game_obj = user_obj.themes_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    themes_kb = user_obj.themes_kb

    await bot.send_message(chat_id=message.from_user.id,
                           text=user_lang_code_object.themes["make choice"],
                           reply_markup=themes_kb.kb_themes)


@dp.callback_query_handler(themes_kb.cb_themes.filter(action=["school",
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
                                                              "hard choice",
                                                              "main menu"]),
                           state=ThemesStates.theme_choice)
async def themes_choice(query: CallbackQuery, callback_data: typing.Dict[str, str]):

    await dp.storage.set_state(chat=query.message.chat.id, user=query.from_user.id, state=ThemesStates.confirmation)
    answer = callback_data['action']


    user_obj = Database.retrieve_user_obj(query.from_user.id)
    themes_game_obj = user_obj.themes_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    themes_kb = user_obj.themes_kb

    message_id = query.message.message_id

    if answer == "main menu":
        await dp.storage.finish(chat=query.message.chat.id, user=query.from_user.id)
        await bot.edit_message_text(chat_id=query.from_user.id,
                               text=user_lang_code_object.info["main_menu"],
                               message_id=message_id, reply_markup=None, parse_mode='HTML')
    else:
        themes_game_obj.theme_chosen = answer
        key = answer + " desc"

        await bot.edit_message_text(text=f"{user_lang_code_object.themes[key]}", chat_id=query.from_user.id, message_id=message_id,
                                            reply_markup=themes_kb.kb_themes_confirm, parse_mode='HTML')


@dp.callback_query_handler(themes_kb.cb_themes_confirm.filter(action=["menu", "begin"]), state=ThemesStates.confirmation)
async def themes_confirm(query: CallbackQuery, callback_data: typing.Dict[str, str]):

    answer = callback_data['action']
    message_id = query.message.message_id

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    themes_game_obj = user_obj.themes_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    themes_kb = user_obj.themes_kb

    if answer == "menu":
        await dp.storage.set_state(chat=query.message.chat.id, user=query.from_user.id, state=ThemesStates.theme_choice)
        themes_game_obj.theme_chosen = ""
        await bot.edit_message_text(text=user_lang_code_object.themes["make choice"],
                                    chat_id=query.from_user.id,
                                    message_id=message_id,
                                    reply_markup=themes_kb.kb_themes,
                                    parse_mode='HTML')
    elif answer == "begin":
        await dp.storage.set_state(chat=query.message.chat.id, user=query.from_user.id, state=ThemesStates.game)
        themes_game_obj.theme()
        themes_game_obj.index = 0
        current_question = themes_game_obj.theme_questions_list[themes_game_obj.index]
        await bot.edit_message_text(text=f"{current_question}",
                                    chat_id=query.from_user.id,
                                    message_id=message_id,
                                    reply_markup=themes_kb.kb_themes_game,
                                    parse_mode='HTML')

@dp.callback_query_handler(themes_kb.cb_themes_game.filter(action=["next", "previous", "end"]), state=ThemesStates.game)
async def themes_game(query: CallbackQuery, callback_data: typing.Dict[str, str]):

    answer = callback_data['action']
    message_id = query.message.message_id

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    themes_game_obj = user_obj.themes_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    themes_kb = user_obj.themes_kb

    if answer == "next":
        if themes_game_obj.index > len(themes_game_obj.theme_questions_list)-1:
            themes_game_obj.theme_chosen = ""
            await bot.edit_message_text(text=user_lang_code_object.themes["game over"],
                                        chat_id=query.from_user.id,
                                        message_id=message_id,
                                        reply_markup=themes_kb.kb_themes,
                                        parse_mode='HTML')
        else:
            themes_game_obj.index += 1
            current_question = themes_game_obj.theme_questions_list[themes_game_obj.index]
            await bot.edit_message_text(text=f"{current_question}",
                                        chat_id=query.from_user.id,
                                        message_id=message_id,
                                        reply_markup=themes_kb.kb_themes_game,
                                        parse_mode='HTML')
    elif answer == "previous":
        if themes_game_obj.index == 0:
            pass

        else:
            themes_game_obj.index -= 1
            current_question = themes_game_obj.theme_questions_list[themes_game_obj.index]
            await bot.edit_message_text(text=f"{current_question}",
                                        chat_id=query.from_user.id,
                                        message_id=message_id,
                                        reply_markup=themes_kb.kb_themes_game,
                                        parse_mode='HTML')
    elif answer == "end":
        await dp.storage.finish(chat=query.message.chat.id, user=query.from_user.id)
        themes_game_obj.theme_chosen = ""
        await bot.edit_message_text(text=user_lang_code_object.themes["game over"]+" /themes",
                                    chat_id=query.from_user.id,
                                    message_id=message_id,
                                    reply_markup=None,
                                    parse_mode='HTML')
        await bot.send_message(text=user_lang_code_object.info["main_menu"], chat_id=query.from_user.id, parse_mode='HTML')