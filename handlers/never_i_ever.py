import logging
import typing

from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from mainUnit.engine import Engine, Users
from mainUnit.keyboards import Keyboards, NieKeyboard
from mainUnit.players import Players
from mainUnit.states import NieStates

from local.lang import Texts

from loader import dp, bot

###

####

logging.basicConfig(level=logging.INFO)

engine = Engine()
player = Players()
# keyboards = Keyboards()
keyboards = NieKeyboard()

###

# players_are_added = False
levels_are_chosen = False
# mode_is_chosen = False

# truth = ""
# truth_index = 0
# dare = ""
# dare_index = 0
# nie_index = 0


nie = ""
tord = ""
tord_t = True

# current_player_name = ""

###

# texts = Texts.never_i_ever

@dp.message_handler(commands="never_i_ever")
async def never_i_ever(message: Message):
    await NieStates.levels.set()
    await Texts.ensure_localisation(Users.get_user_lang_code(message.from_user.id))
    await bot.send_message(chat_id=message.from_user.id, text=Texts.never_i_ever["choose levels"], reply_markup=keyboards.keyboard_level_all)


@dp.callback_query_handler(keyboards.cb_all_level.filter(action=['lifestyle', 'absurd', 'company', 'relations', 'awkward', 'ready']), state=NieStates.levels)
async def nie_levels(query: CallbackQuery, state: FSMContext, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    answer = callback_data['action']
    if answer == 'lifestyle':
        new_keyboard = keyboards.update_keyboard(0, query.message.reply_markup)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'absurd':
        new_keyboard = keyboards.update_keyboard(1, query.message.reply_markup)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'company':
        new_keyboard = keyboards.update_keyboard(2, query.message.reply_markup)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'relations':
        new_keyboard = keyboards.update_keyboard(3, query.message.reply_markup)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'awkward':
        new_keyboard = keyboards.update_keyboard(4, query.message.reply_markup)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'ready':
        if not True in [keyboards.lifestyle_level, keyboards.absurd_level, keyboards.relations_level, keyboards.personal_level, keyboards.adult_level]:
            await bot.answer_callback_query(query.id, Texts.never_i_ever["no choice made"], True)
        else:
            await NieStates.game.set()
            engine.set_levels(keyboards.lifestyle_level, keyboards.absurd_level, keyboards.relations_level, keyboards.personal_level, keyboards.adult_level)
            await bot.send_message(chat_id=query.from_user.id,
                                   text=Texts.never_i_ever["begin it"],
                                   reply_markup=keyboards.keyboard_nie)
    global levels_are_chosen
    if True in [keyboards.lifestyle_level, keyboards.absurd_level, keyboards.relations_level, keyboards.personal_level, keyboards.adult_level]:
        levels_are_chosen = True
    else:
        levels_are_chosen = False


@dp.callback_query_handler(keyboards.cb_nie.filter(action=['truth_nie', 'dare_nie', 'next_nie', 'end_nie']),
                           state=NieStates.game)
async def nie_game(query: CallbackQuery, state: FSMContext, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    answer = callback_data['action']
    global tord, tord_t, nie
    if answer == 'truth_nie':
        tord_t = True
        tord = engine.shuffled_list(engine.t_all)[0]
        await bot.edit_message_text(text=tord, reply_markup=keyboards.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)
    elif answer == 'dare_nie':
        tord_t = False
        tord = engine.shuffled_list(engine.d_all)[0]
        await bot.edit_message_text(text=tord, reply_markup=keyboards.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)
    elif answer == 'next_nie':
        nie = engine.shuffled_list(engine.n_all)[0]
        await bot.edit_message_text(text=nie, reply_markup=keyboards.keyboard_nie,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)
        engine.n_all.remove(nie)
    elif answer == 'end_nie':
        await state.finish()
        await bot.send_message(chat_id=query.from_user.id,
                               text=Texts.never_i_ever["game over"])


@dp.callback_query_handler(keyboards.cb_completed_f.filter(action=['completed_f', 'failed_f']),
                           state=NieStates.game)
async def nie_comp(query: CallbackQuery, state: FSMContext, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    answer = callback_data['action']
    global tord, tord_t, nie
    if answer == 'completed_f':
        if tord_t == True:
            engine.t_all.remove(tord)
        elif tord_t == False:
            engine.d_all.remove(tord)
        await bot.edit_message_text(chat_id=query.from_user.id, text=nie,
                               reply_markup=keyboards.keyboard_nie, message_id=query.message.message_id)

    elif answer == 'failed_f':
        if tord_t == True:
            tord = engine.shuffled_list(engine.t_all)[0]
        elif tord_t == False:
            tord = engine.shuffled_list(engine.d_all)[0]
        await bot.edit_message_text(text=tord, reply_markup=keyboards.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)