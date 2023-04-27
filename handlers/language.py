import typing

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from mainUnit.users import loc_objects

from mainUnit.engine import Users
from mainUnit.keyboards import ConfigKeyboard
from mainUnit.states import LangStates
from mainUnit.database import Database
from mainUnit.games import Tord, Nie, ThreeOfFive, Themes
from mainUnit.keyboards import TordKeyboard, NieKeyboard, ThemesKeyboard, ThreeOfFiveKeyboard
from mainUnit.users import Users
from local.lang import Texts


@dp.message_handler(commands="language")
async def language(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text="Choose language/Выбери язык", reply_markup=ConfigKeyboard.kb_lang)
    # await LangStates.pending.set()
    await dp.storage.set_state(chat=message.chat.id, user=message.from_user.id, state=LangStates.pending)

@dp.callback_query_handler(ConfigKeyboard.cb_lang.filter(action=['en', 'de', 'fr', 'es', 'sr', 'ru', 'uk']), state=LangStates.pending)
async def choose_language(query: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):

    lang_code_choice = callback_data['action']
    print(lang_code_choice)

    responses = {'en': "English language chosen as a default. Have a nice game!",
                'de': "Standardmäßig ist die deutsche Sprache gewählt. Haben Sie ein schönes Spiel!",
                'fr': "Langue française choisie par défaut. Bon jeu!",
                'es': "Idioma español elegido por defecto. ¡Que tengas un buen juego!",
                'sr': "Српски језик изабран као подразумевани. Угодна игра!",
                'ru': "Русский язык выбран по умолчанию. Приятной игры!",
                'uk': "За замовчуванням обрано українську мову. Гарної гри!"
    }

    loc_obj = loc_objects[lang_code_choice]
    print(loc_obj.keyboards)


    updated_user_obj = Users(
        user_id=query.from_user.id,
        lang_code=lang_code_choice,
        tord_game=Tord(query.from_user.id, lang_code_choice),
        nie_game=Nie(query.from_user.id, lang_code_choice),
        the_35_game=ThreeOfFive(query.from_user.id, lang_code_choice),
        themes_game=Themes(query.from_user.id, lang_code_choice),
        tord_kb=TordKeyboard(loc_obj),
        nie_kb=NieKeyboard(loc_obj),
        the_35_kb=ThreeOfFiveKeyboard(loc_obj),
        themes_kb=ThemesKeyboard(loc_obj),
        chat_id=query.message.chat.id,
        chat_type=query.message.chat.type,
        username=query.from_user.username,
        fName=query.from_user.first_name,
        lName=query.from_user.last_name,
        is_bot=query.from_user.is_bot
    )

    Database.update_user_obj(query.from_user.id, updated_user_obj)

    user_obj = Database.retrieve_user_obj(query.from_user.id)

    user_lang_code_object = loc_objects[user_obj.lang_code]
    # user_lang_code_object.load_localisation()  # load localisation files

    await bot.edit_message_text(text=f"{responses[lang_code_choice]}",
                                chat_id=query.message.chat.id, message_id=query.message.message_id,
                                reply_markup=None)
    await bot.send_message(text=user_lang_code_object.info['main_menu'], chat_id=query.from_user.id, parse_mode='HTML')
    await dp.storage.finish(chat=query.message.chat.id, user=query.from_user.id)
