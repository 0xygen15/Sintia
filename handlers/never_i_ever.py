import logging
import typing

from aiogram.types import CallbackQuery, Message

from mainUnit.states import NieStates
from mainUnit.users import loc_objects
from mainUnit.keyboards import NieKeyboard
from mainUnit.database import Database

from loader import dp, bot

###

####

logging.basicConfig(level=logging.INFO)

###
nie_kb: NieKeyboard = NieKeyboard(loc_file=loc_objects["en"])
# texts = Texts.never_i_ever

@dp.message_handler(commands="never_i_ever", state='*')
async def never_i_ever(message: Message, state: FSMContext):
    # global keyboards, engine, player
    # await state.finish()
    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)
    # await NieStates.levels.set()
    await dp.storage.set_state(chat=message.chat.id, user=message.from_user.id, state=NieStates.levels)
    # Texts.ensure_localisation(Users.get_user_lang_code(message.from_user.id))
    # keyboards, engine, player = update_keyboards_object()
    user_obj = Database.retrieve_user_obj(message.from_user.id)
    nie_game_obj = user_obj.nie_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    nie_kb = user_obj.nie_kb
    # keyboards, engine, player = NieKeyboard(), Engine(), Players()
    await bot.send_message(chat_id=message.from_user.id, text=user_lang_code_object.never_i_ever["choose levels"], reply_markup=nie_kb.keyboard_level_all)


@dp.callback_query_handler(nie_kb.cb_all_level.filter(action=['lifestyle', 'absurd', 'company', 'relations', 'awkward', 'ready']), state=NieStates.levels)
async def nie_levels(query: CallbackQuery, state: FSMContext, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    answer = callback_data['action']

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    nie_game_obj = user_obj.nie_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    nie_kb = user_obj.nie_kb

    if answer == 'lifestyle':
        new_keyboard = nie_kb.update_keyboard(0, query.message.reply_markup, nie_game_obj)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'absurd':
        new_keyboard = nie_kb.update_keyboard(1, query.message.reply_markup, nie_game_obj)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'company':
        new_keyboard = nie_kb.update_keyboard(2, query.message.reply_markup, nie_game_obj)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'relations':
        new_keyboard = nie_kb.update_keyboard(3, query.message.reply_markup, nie_game_obj)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'awkward':
        new_keyboard = nie_kb.update_keyboard(4, query.message.reply_markup, nie_game_obj)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'ready':
        if not True in [keyboards.lifestyle_level, keyboards.absurd_level, keyboards.relations_level, keyboards.personal_level, keyboards.adult_level]:
            await bot.answer_callback_query(query.id, Texts.never_i_ever["no choice made"], True)
        else:
            # await NieStates.game.set()
            await dp.storage.set_state(chat=message.chat.id, user=message.from_user.id, state=NieStates.game)
            nie_game_obj.set_levels()
            await bot.send_message(chat_id=query.from_user.id,
                                   text=user_lang_code_object.never_i_ever["begin it"],
                                   reply_markup=keyboards.keyboard_nie)
    # global levels_are_chosen
    # if True in [keyboards.lifestyle_level, keyboards.absurd_level, keyboards.relations_level, keyboards.personal_level, keyboards.adult_level]:
    #     levels_are_chosen = True
    # else:
    #     levels_are_chosen = False


@dp.callback_query_handler(nie_kb.cb_nie.filter(action=['truth_nie', 'dare_nie', 'next_nie', 'end_nie']),
                           state=NieStates.game)
async def nie_game(query: CallbackQuery, state: FSMContext, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    nie_game_obj = user_obj.nie_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    nie_kb = user_obj.nie_kb

    answer = callback_data['action']
    # global tord, tord_t, nie
    if answer == 'truth_nie':
        nie_game_obj.tord_truth = True
        nie_game_obj.shuffle_lists()
        nie_game_obj.tord = nie_game_obj.truths_list[0]
        await bot.edit_message_text(text=nie_game_obj.tord, reply_markup=nie_kb.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)
    elif answer == 'dare_nie':
        nie_game_obj.tord_truth = False
        nie_game_obj.tord = nie_game_obj.shuffle_lists()[0]
        await bot.edit_message_text(text=nie_game_obj.tord, reply_markup=nie_kb.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)
    elif answer == 'next_nie':
        nie_game_obj.nie = nie_game_obj.nevers_list[0]
        await bot.edit_message_text(text=nie, reply_markup=nie_kb.keyboard_nie,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)
        nie_game_obj.nevers_list.remove(nie_game_obj.nie)
    elif answer == 'end_nie':
        # await state.finish()
        await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)
        await bot.send_message(chat_id=query.from_user.id,
                               text=user_lang_code_object.never_i_ever["game over"])
        await bot.send_message(text=user_lang_code_object.info["main_menu"], chat_id=query.from_user.id, parse_mode='HTML')


@dp.callback_query_handler(keyboards.cb_completed_f.filter(action=['completed_f', 'failed_f']),
                           state=NieStates.game)
async def nie_comp(query: CallbackQuery, state: FSMContext, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    nie_game_obj = user_obj.nie_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    nie_kb = user_obj.nie_kb

    answer = callback_data['action']
    # global tord, tord_t, nie
    if answer == 'completed_f':
        if nie_game_obj.tord_truth == True:
            nie_game_obj.truths_list.remove(nie_game_obj.tord)
        elif nie_game_obj.tord_truth == False:
            nie_game_obj.dares_list.remove(nie_game_obj.tord)
        await bot.edit_message_text(chat_id=query.from_user.id, text=nie_game_obj.nie,
                               reply_markup=keyboards.keyboard_nie, message_id=query.message.message_id)

    elif answer == 'failed_f':
        if nie_game_obj.tord_truth == True:
            nie_game_obj.shuffle_lists()
            nie_game_obj.tord = nie_game_obj.truths_list[0]
        elif nie_game_obj.tord_truth == False:
            nie_game_obj.tord = nie_game_obj.dares_list[0]
        await bot.edit_message_text(text=nie_game_obj.tord, reply_markup=nie_kb.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)