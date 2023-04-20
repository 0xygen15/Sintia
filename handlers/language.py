import typing

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from mainUnit.engine import Users
from mainUnit.keyboards import ConfigKeyboard
from mainUnit.states import LangStates

from local.lang import Texts

@dp.message_handler(commands="language")
async def language(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text="Choose language/Выбери язык", reply_markup=ConfigKeyboard.kb_lang)
    await LangStates.pending.set()

@dp.callback_query_handler(ConfigKeyboard.cb_lang.filter(action=['en', 'de', 'fr', 'es', 'sr', 'ru', 'uk']),
                           state=LangStates.pending)
async def choose_language(query: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):
    lang_code_choice = callback_data['action']
    responses = {'en': "English language chosen as a default. Have a nice game!",
                'de': "Standardmäßig ist die deutsche Sprache gewählt. Haben Sie ein schönes Spiel!",
                'fr': "Langue française choisie par défaut. Bon jeu!",
                'es': "Idioma español elegido por defecto. ¡Que tengas un buen juego!",
                'sr': "Српски језик изабран као подразумевани. Угодна игра!",
                'ru': "Русский язык выбран по умолчанию. Приятной игры!",
                'uk': "За замовчуванням обрано українську мову. Гарної гри!"
    }

    Users.change_user_lang_code(lang_code_choice, query.from_user.id)
    Texts.lang_code = Users.get_user_lang_code(query.from_user.id)
    Texts.load_localisation(Texts.lang_code)
    await bot.edit_message_text(text=f"{responses[lang_code_choice]}",
                                chat_id=query.message.chat.id, message_id=query.message.message_id,
                                reply_markup=None)
    await bot.send_message(text=Texts.info['main_menu'], chat_id=query.from_user.id, parse_mode='HTML')
    await state.finish()

    # if answer == 'en':
    #     Users.change_user_lang_code('en', query.from_user.id)
    #     Texts.lang_code = Users.get_user_lang_code(query.from_user.id)
    #     Texts.load_localisation(Texts.lang_code)
    #     await bot.edit_message_text(text="English language chosen as a default. Have a nice game!",
    #                                 chat_id=query.message.chat.id, message_id=query.message.message_id,
    #                                 reply_markup=None)
    #     await state.finish()
    # elif answer == 'de':
    #     Users.change_user_lang_code('de', query.from_user.id)
    #     Texts.lang_code = Users.get_user_lang_code(query.from_user.id)
    #     Texts.load_localisation(Texts.lang_code)
    #     await bot.edit_message_text(text="Standardmäßig ist die deutsche Sprache gewählt. Haben Sie ein schönes Spiel!",
    #                                 chat_id=query.message.chat.id, message_id=query.message.message_id,
    #                                 reply_markup=None)
    #     await state.finish()
    # elif answer == 'fr':
    #     Users.change_user_lang_code('fr', query.from_user.id)
    #     Texts.lang_code = Users.get_user_lang_code(query.from_user.id)
    #     Texts.load_localisation(Texts.lang_code)
    #     await bot.edit_message_text(text="Langue française choisie par défaut. Bon jeu !", chat_id=query.message.chat.id,
    #                                 message_id=query.message.message_id,
    #                                 reply_markup=None)
    #     await state.finish()
    # elif answer == 'es':
    #     Users.change_user_lang_code('es', query.from_user.id)
    #     Texts.lang_code = Users.get_user_lang_code(query.from_user.id)
    #     Texts.load_localisation(Texts.lang_code)
    #     await bot.edit_message_text(text="Idioma español elegido por defecto. ¡Que tengas un buen juego!",
    #                                 chat_id=query.message.chat.id, message_id=query.message.message_id,
    #                                 reply_markup=None)
    #     await state.finish()
    # elif answer == 'sr':
    #     Users.change_user_lang_code('sr', query.from_user.id)
    #     Texts.lang_code = Users.get_user_lang_code(query.from_user.id)
    #     Texts.load_localisation(Texts.lang_code)
    #     await bot.edit_message_text(text="Српски језик изабран као подразумевани. Угодна игра!",
    #                                 chat_id=query.message.chat.id, message_id=query.message.message_id,
    #                                 reply_markup=None)
    #     await state.finish()
    # elif answer == 'ru':
    #     Users.change_user_lang_code('ru', query.from_user.id)
    #     Texts.lang_code = Users.get_user_lang_code(query.from_user.id)
    #     Texts.load_localisation(Texts.lang_code)
    #     await bot.edit_message_text(text="Русский язык выбран по умолчанию. Приятной игры!",
    #                                 chat_id=query.message.chat.id, message_id=query.message.message_id,
    #                                 reply_markup=None)
    #     await state.finish()
    # elif answer == 'uk':
    #     Users.change_user_lang_code('uk', query.from_user.id)
    #     Texts.lang_code = Users.get_user_lang_code(query.from_user.id)
    #     Texts.load_localisation(Texts.lang_code)
    #     await bot.edit_message_text(text="За замовчуванням вибрано українську мову. Гарної гри!",
    #                                 chat_id=query.message.chat.id, message_id=query.message.message_id,
    #                                 reply_markup=None)
    #     await state.finish()