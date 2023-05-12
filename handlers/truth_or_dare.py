import logging
import typing

from aiogram.types import CallbackQuery, Message

from mainUnit.states import PlayerStates
from mainUnit.users import loc_objects
from mainUnit.keyboards import TordKeyboard
from mainUnit.database import Database

from loader import dp, bot


####

logging.basicConfig(level=logging.INFO)

tord_kb: TordKeyboard = TordKeyboard(loc_file=loc_objects["en"]) #defaul kb, so it would be possible to use decorators

@dp.message_handler(commands='truth_or_dare', state='*')
async def players_names(message: Message):

    await dp.storage.finish(chat=message.chat.id, user=message.from_user.id)
    await dp.storage.set_state(chat=message.chat.id, user=message.from_user.id, state=PlayerStates.ready_to_get_players_names)

    user_obj = Database.retrieve_user_obj(message.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb # it is ok to shadow from outer scope

    tord_game_obj.reset()
    tord_kb.reset()

    tord_game_obj.first_message_id = message.message_id

    await bot.send_message(chat_id=message.from_user.id, text=user_lang_code_object.truth_or_dare["players names enter request"])
    logging.info("User is asked to enter names of players")


@dp.callback_query_handler(tord_kb.to_menu_cb.filter(action=["main menu"]), state=PlayerStates.ready_to_get_players_names)
async def to_main_menu(query: CallbackQuery):
    await dp.storage.finish(chat=query.message.chat.id, user=query.from_user.id)

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb  # it is ok to shadow from outer scope

    tord_game_obj.reset()
    tord_kb.reset()

    message_id_to_edit = query.message.message_id

    await bot.edit_message_text(text=user_lang_code_object.info["main_menu"], chat=query.message.chat.id,
                                message_id=message_id_to_edit, reply_markup=None, parse_mode="HTML")

@dp.message_handler(state=PlayerStates.ready_to_get_players_names)
async def check_players_names(message: Message):
    user_obj = Database.retrieve_user_obj(message.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb # it is ok to shadow from outer scope

    await dp.storage.set_state(chat=message.chat.id, user=message.from_user.id, state=PlayerStates.check_players_names)
    tord_game_obj.add_players_names(message.text)

    names = tord_game_obj.get_str_of_players_list()
    answer = f"""{user_lang_code_object.truth_or_dare["check names"]}\n\n{names}\n{user_lang_code_object.truth_or_dare["right?"]}"""

    if len(tord_game_obj.players_list) < 2:
        tord_game_obj.reset()
        tord_kb.reset()
        await bot.send_message(chat_id=message.from_user.id, text=f"{user_lang_code_object.truth_or_dare['min2']} /truth_or_dare")
        await dp.storage.set_state(chat=message.chat.id, user=message.from_user.id,
                                   state=PlayerStates.ready_to_get_players_names)
        await bot.send_message(chat_id=message.from_user.id,
                               text=user_lang_code_object.truth_or_dare["players names enter request"])
    else:
        await bot.send_message(chat_id=message.from_user.id, text=answer, reply_markup=tord_kb.keyboard_players)
        logging.info(f"User has entered {tord_game_obj.players_list}")


@dp.callback_query_handler(tord_kb.cb_players.filter(action=["main menu"]), state=PlayerStates.check_players_names)
async def to_main_menu(query: CallbackQuery):
    await dp.storage.finish(chat=query.message.chat.id, user=query.from_user.id)

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb  # it is ok to shadow from outer scope

    tord_game_obj.reset()
    tord_kb.reset()

    last_message = query.message.message_id
    for m in range(tord_game_obj.first_message_id, last_message):
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=m)
        except:
            pass

    await bot.send_message(text=user_lang_code_object.info["main_menu"], chat=query.message.chat.id, parse_mode="HTML")



@dp.callback_query_handler(tord_kb.cb_players.filter(action='no'), state=PlayerStates.check_players_names)
async def players_no(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]

    tord_game_obj.players_list.clear()

    last_message = query.message.message_id
    for m in range(tord_game_obj.first_message_id, last_message):
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=m)
        except:
            pass

    await dp.storage.set_state(chat=query.message.chat.id, user=query.from_user.id, state=PlayerStates.ready_to_get_players_names)

    await bot.send_message(chat_id=query.from_user.id, text=user_lang_code_object.truth_or_dare["enter usernames"])
    logging.info("User reenters names")


@dp.callback_query_handler(tord_kb.cb_players.filter(action='yes'), state=PlayerStates.check_players_names)
async def players_yes(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb # it is ok to shadow from outer scope

    tord_game_obj.players_are_added = True

    last_message = query.message.message_id
    for m in range(tord_game_obj.first_message_id, last_message - 1):
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=m)
        except:
            pass

    # await bot.send_message(chat_id=query.from_user.id, text=user_lang_code_object.truth_or_dare["proceed to settings"])
    await dp.storage.set_state(chat=query.message.chat.id, user=query.from_user.id, state=PlayerStates.settings)
    text = f"""{user_lang_code_object.truth_or_dare["proceed to settings"]}\n\n{user_lang_code_object.truth_or_dare["choose levels"]}"""
    # await bot.send_message(text=user_lang_code_object.truth_or_dare["choose levels"],
    #                        chat_id=query.from_user.id,
    #                        reply_markup=tord_kb.keyboard_level_all)
    await bot.edit_message_text(text=text,
                           chat_id=query.from_user.id,
                           reply_markup=tord_kb.keyboard_level_all,
                           message_id=last_message,
                           parse_mode="HTML")
    logging.info(f"User has is offered to choose levels")



@dp.callback_query_handler(tord_kb.cb_all_level.filter(action=['lifestyle', 'absurd', 'company', 'relations', 'awkward', 'ready']),
                           state=PlayerStates.settings)
async def settings(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    user_obj = Database.retrieve_user_obj(query.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb # it is ok to shadow from outer scope

    answer = callback_data['action']
    if answer == 'lifestyle':
        new_keyboard = tord_kb.update_keyboard(0, query.message.reply_markup, tord_game_obj)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'absurd':
        new_keyboard = tord_kb.update_keyboard(1, query.message.reply_markup, tord_game_obj)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'company':
        new_keyboard = tord_kb.update_keyboard(2, query.message.reply_markup, tord_game_obj)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'relations':
        new_keyboard = tord_kb.update_keyboard(3, query.message.reply_markup, tord_game_obj)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'awkward':
        new_keyboard = tord_kb.update_keyboard(4, query.message.reply_markup, tord_game_obj)
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            reply_markup=new_keyboard,
                                            message_id=query.message.message_id)
    elif answer == 'ready':
        if not True in [tord_game_obj.lifestyle_level, tord_game_obj.absurd_level, tord_game_obj.relations_level, tord_game_obj.personal_level, tord_game_obj.adult_level]:
            await bot.answer_callback_query(query.id, user_lang_code_object.never_i_ever["no choice made"], True)
        else:
            # await PlayerStates.mode.set()
            await dp.storage.set_state(chat=query.message.chat.id, user=query.from_user.id, state=PlayerStates.mode)
            message_id_to_edit = query.message.message_id
            # await bot.send_message(chat_id=query.from_user.id,
            #                        text=user_lang_code_object.truth_or_dare["mode"],
            #                        reply_markup=tord_kb.keyboard_mode)
            await bot.edit_message_text(chat_id=query.from_user.id,
                                   text=user_lang_code_object.truth_or_dare["mode"],
                                   reply_markup=tord_kb.keyboard_mode,
                                   message_id=message_id_to_edit,
                                   parse_mode="HTML")


    if True in [tord_kb.lifestyle_level, tord_kb.absurd_level, tord_kb.relations_level, tord_kb.personal_level, tord_kb.adult_level]:
        tord_game_obj.levels_are_chosen = True
    else:
        tord_game_obj.levels_are_chosen = False



@dp.callback_query_handler(tord_kb.cb_mode.filter(action=['free', 'step']), state=PlayerStates.mode)
async def mode(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    user_obj = Database.retrieve_user_obj(query.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb # it is ok to shadow from outer scope

    answer = callback_data['action']

    tord_game_obj.last_message_id = query.message.message_id
    if answer == 'free':
        await dp.storage.set_state(chat=query.message.chat.id, user=query.from_user.id, state=PlayerStates.game_free)
        # await PlayerStates.game_free.set()
        tord_game_obj.set_levels()
        tord_game_obj.current_player_name = tord_game_obj.players_list[tord_game_obj.current_player_number]
        message_id_to_edit = query.message.message_id
        # await bot.send_message(chat_id=query.from_user.id, text=f'{tord_game_obj.current_player_name}, {user_lang_code_object.truth_or_dare["tord?"]}',
        #                        reply_markup=tord_kb.keyboard_td)
        await bot.edit_message_text(chat_id=query.from_user.id,
                               text=f'{tord_game_obj.current_player_name}, {user_lang_code_object.truth_or_dare["tord?"]}',
                               reply_markup=tord_kb.keyboard_td,
                               message_id=message_id_to_edit,
                               parse_mode="HTML")
        # try:
        #     for mid in range(tord_game_obj.first_message_id, tord_game_obj.last_message_id+1):
        #         await bot.delete_message(chat_id=query.from_user.id, message_id=mid)
        # except:
        #     pass

    elif answer == 'step':
        if tord_game_obj.levels_are_chosen == False and tord_game_obj.players_are_added == False:
            await bot.send_message(chat_id=query.from_user.id,
                                   text=user_lang_code_object.truth_or_dare["players, level and mode!"])
        else:
            await dp.storage.set_state(chat=query.message.chat.id, user=query.from_user.id, state=PlayerStates.game)
            tord_game_obj.set_levels()
            tord_game_obj.current_player_name = tord_game_obj.players_list[tord_game_obj.current_player_number]
            if tord_game_obj.truth_circle == True:
                tord_game_obj.shuffle_lists()
                tord_game_obj.truth = tord_game_obj.truths_list[0]
                message_id_to_edit = query.message.message_id
                # await bot.send_message(chat_id=query.from_user.id,
                #                        text=f"{tord_game_obj.current_player_name}, {tord_game_obj.truth}",
                #                        reply_markup=tord_kb.keyboard_completed)
                await bot.edit_message_text(chat_id=query.from_user.id,
                                       text=f"{tord_game_obj.current_player_name}, {tord_game_obj.truth}",
                                       reply_markup=tord_kb.keyboard_completed,
                                       message_id=message_id_to_edit,
                                       parse_mode="HTML")
                # try:
                #     for mid in range(tord_game_obj.first_message_id, tord_game_obj.last_message_id+1):
                #         await bot.delete_message(chat_id=query.from_user.id, message_id=mid)
                # except:
                #     pass
                logging.info(
                    f"Truth circle = {tord_game_obj.truth_circle}; "
                    f"Current player name: {tord_game_obj.current_player_name}; "
                    f"Truth: {tord_game_obj.truth}")
            elif tord_game_obj.truth_circle == False:
                tord_game_obj.shuffle_lists()
                tord_game_obj.dare = tord_game_obj.dares_list[0]
                message_id_to_edit = query.message.message_id
                # await bot.send_message(chat_id=query.from_user.id,
                #                        text=f"{tord_game_obj.current_player_name}, {tord_game_obj.dare}",
                #                        reply_markup=tord_kb.keyboard_completed)
                await bot.edit_message_text(chat_id=query.from_user.id,
                                       text=f"{tord_game_obj.current_player_name}, {tord_game_obj.dare}",
                                       reply_markup=tord_kb.keyboard_completed,
                                       message_id=message_id_to_edit,
                                       parse_mode="HTML")
                # try:
                #     for mid in range(tord_game_obj.first_message_id, tord_game_obj.last_message_id+1):
                #         await bot.delete_message(chat_id=query.from_user.id, message_id=mid)
                # except:
                #     pass
                logging.info(
                    f"Truth circle = {tord_game_obj.truth_circle};"
                    f"Current player name: {tord_game_obj.current_player_name};"
                    f"Dare: {tord_game_obj.dare};")



@dp.callback_query_handler(tord_kb.cb_completed.filter(action=['completed', 'failed', 'over']),
                           state=PlayerStates.game)
async def game_step(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    user_obj = Database.retrieve_user_obj(query.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb # it is ok to shadow from outer scope

    answer = callback_data['action']
    message_id = query.message.message_id

    if answer == 'completed':
        tord_game_obj.next_player_number()
        tord_game_obj.circle_changer()

        if tord_game_obj.out_of_objects() == True: #GAME WILL GO ON UNTIL USER STOPS THE GAME
            # await dp.storage.finish(chat=query.message.chat.id, user=query.from_user.id)

            # message_id_to_edit = query.message.message_id

            tord_game_obj.load_again()
            tord_game_obj.current_player_name = tord_game_obj.players_list[tord_game_obj.current_player_number]
            tord_game_obj.shuffle_lists()

            if tord_game_obj.truth_circle == True:
                tord_game_obj.truth = tord_game_obj.truths_list[0]
                await bot.edit_message_text(chat_id=query.from_user.id,
                                            text=f"{tord_game_obj.current_player_name}, {tord_game_obj.truth}",
                                            reply_markup=tord_kb.keyboard_completed,
                                            message_id=message_id)
            else:
                tord_game_obj.shuffle_lists()
                tord_game_obj.dare = tord_game_obj.dares_list[0]
                await bot.edit_message_text(chat_id=query.from_user.id,
                                            text=f"{tord_game_obj.current_player_name}, {tord_game_obj.dare}",
                                            reply_markup=tord_kb.keyboard_completed,
                                            message_id=message_id)
            # await bot.send_message(chat_id=query.from_user.id,
            #                        text=f"{user_lang_code_object.truth_or_dare['game over']} /truth_or_dare")
            await bot.edit_message_text(chat_id=query.from_user.id,
                                   text=f"{user_lang_code_object.truth_or_dare['game over']} /truth_or_dare",
                                        message_id=message_id,
                                        reply_markup=None,
                                        parse_mode="HTML")

        if tord_game_obj.truth_circle == True:
            tord_game_obj.truths_list.remove(tord_game_obj.truth)
            tord_game_obj.current_player_name = tord_game_obj.players_list[tord_game_obj.current_player_number]
            tord_game_obj.shuffle_lists()
            tord_game_obj.truth = tord_game_obj.truths_list[0]
            await bot.edit_message_text(chat_id=query.from_user.id,
                                   text=f"{tord_game_obj.current_player_name}, {tord_game_obj.truth}",
                                   reply_markup=tord_kb.keyboard_completed,
                                   message_id = message_id)
            logging.info(
                f"\nTruth circle = {tord_game_obj.truth_circle}; "
                f"Current player name: {tord_game_obj.current_player_name}; "
                f"Current player number: {tord_game_obj.current_player_number};\n"
                f"Current q: {tord_game_obj.truth};\n"
                f"Length o lust: {len(tord_game_obj.truths_list)}")

        elif tord_game_obj.truth_circle == False:
            try:
                tord_game_obj.dares_list.remove(tord_game_obj.dare)
            except ValueError:
                pass
            tord_game_obj.current_player_name = tord_game_obj.players_list[tord_game_obj.current_player_number]
            tord_game_obj.shuffle_lists()
            tord_game_obj.dare = tord_game_obj.dares_list[0]
            await bot.edit_message_text(chat_id=query.from_user.id,
                                   text=f"{tord_game_obj.current_player_name}, {tord_game_obj.dare}",
                                   reply_markup=tord_kb.keyboard_completed,
                                   message_id = message_id)

            logging.info(
                f"\nTruth circle = {tord_game_obj.truth_circle}; "
                f"Current player name: {tord_game_obj.current_player_name}; "
                f"Current player number: {tord_game_obj.current_player_number};\n"
                f"Current q: {tord_game_obj.dare};\n"
                f"Length o lust: {len(tord_game_obj.dares_list)}")

    elif answer == 'failed':
        if tord_game_obj.fail_check(tord_game_obj.current_player_name) == True:
            await bot.answer_callback_query(query.id,
                                            f'{tord_game_obj.current_player_name}, {user_lang_code_object.truth_or_dare["penalty"]}',
                                            True)
        tord_game_obj.penalties[tord_game_obj.current_player_name] += 1
        if tord_game_obj.truth_circle == True:
            tord_game_obj.shuffle_lists()
            tord_game_obj.truth = tord_game_obj.truths_list[0]
            await bot.edit_message_text(chat_id=query.from_user.id,
                                   text=f"{tord_game_obj.current_player_name}, {tord_game_obj.truth}",
                                   reply_markup=tord_kb.keyboard_completed,
                                   message_id=query.message.message_id)
        elif tord_game_obj.truth_circle == False:
            tord_game_obj.shuffle_lists()
            tord_game_obj.dare = tord_game_obj.dares_list[0]
            await bot.edit_message_text(chat_id=query.from_user.id,
                                        text=f"{tord_game_obj.current_player_name}, {tord_game_obj.dare}",
                                        reply_markup=tord_kb.keyboard_completed,
                                        message_id=query.message.message_id)

    elif answer == "over":
        await dp.storage.finish(chat=query.message.chat.id, user=query.from_user.id)

        tord_game_obj.reset()
        tord_kb.reset()

        # message_id_to_edit = query.message.message_id

        # await bot.send_message(chat_id=query.from_user.id,
        #                        text=f"{user_lang_code_object.truth_or_dare['game over']} /truth_or_dare")
        # await bot.edit_message_text(chat_id=query.from_user.id,
        #                        text=f"{user_lang_code_object.truth_or_dare['game over']}",
        #                             message_id=message_id_to_edit,
        #                             reply_markup=None,
        #                             parse_mode="HTML")

        await bot.send_message(text=user_lang_code_object.info["main_menu"], chat_id=query.from_user.id, parse_mode='HTML')
        await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)



@dp.callback_query_handler(tord_kb.cb_td.filter(action=['truth', 'dare', 'end']),
                           state=PlayerStates.game_free)
async def game_free(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb # it is ok to shadow from outer scope

    answer = callback_data['action']

    tord_game_obj.current_player_name = tord_game_obj.players_list[tord_game_obj.current_player_number]
    if answer == 'truth':
        tord_game_obj.shuffle_lists()
        tord_game_obj.td_obj_truth = True
        tord_game_obj.td_obj = tord_game_obj.truths_list[0]
        await bot.edit_message_text(text=f"{tord_game_obj.current_player_name}, {tord_game_obj.td_obj}", reply_markup=tord_kb.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)
    elif answer == 'dare':
        tord_game_obj.shuffle_lists()
        tord_game_obj.td_obj_truth = False
        tord_game_obj.td_obj = tord_game_obj.dares_list[0]
        await bot.edit_message_text(text=f"{tord_game_obj.current_player_name}, {tord_game_obj.td_obj}", reply_markup=tord_kb.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)
    elif answer == 'end':
        tord_game_obj.reset()
        tord_kb.reset()

        await dp.storage.finish(chat=query.message.chat.id, user=query.from_user.id)

        # message_id_to_edit = query.message.message_id
        #
        # await bot.edit_message_text(chat_id=query.from_user.id,
        #                             text=f"{user_lang_code_object.truth_or_dare['game over']}",
        #                             message_id=message_id_to_edit,
        #                             reply_markup=None,
        #                             parse_mode="HTML")

        await bot.send_message(text=user_lang_code_object.info["main_menu"], chat_id=query.from_user.id, parse_mode='HTML')
        await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)



@dp.callback_query_handler(tord_kb.cb_completed_f.filter(action=['completed_f', 'failed_f']),
                           state=PlayerStates.game_free)
async def game_free_c(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)

    user_obj = Database.retrieve_user_obj(query.from_user.id)
    tord_game_obj = user_obj.tord_game
    user_lang_code_object = loc_objects[user_obj.lang_code]
    tord_kb = user_obj.tord_kb # it is ok to shadow from outer scope

    answer = callback_data['action']

    if answer == 'completed_f':
        if tord_game_obj.td_obj_truth == True:
            tord_game_obj.truths_list.remove(tord_game_obj.td_obj)
        elif tord_game_obj.td_obj_truth == False:
            tord_game_obj.dares_list.remove(tord_game_obj.td_obj)
        tord_game_obj.next_player_number()
        tord_game_obj.current_player_name = tord_game_obj.players_list[tord_game_obj.current_player_number]
        await bot.edit_message_text(chat_id=query.from_user.id, text=f'{tord_game_obj.current_player_name}, {user_lang_code_object.truth_or_dare["tord?"]}',
                               reply_markup=tord_kb.keyboard_td, message_id=query.message.message_id)

    elif answer == 'failed_f':
        if tord_game_obj.fail_check(tord_game_obj.current_player_name) == True:
            await bot.answer_callback_query(query.id,
                                            f'{tord_game_obj.current_player_name}, {user_lang_code_object.truth_or_dare["penalty"]}',
                                            True)
        tord_game_obj.penalties[tord_game_obj.current_player_name] += 1
        if tord_game_obj.td_obj_truth == True:
            tord_game_obj.shuffle_lists()
            tord_game_obj.td_obj = tord_game_obj.truths_list[0]
        elif tord_game_obj.td_obj_truth == False:
            tord_game_obj.shuffle_lists()
            tord_game_obj.td_obj = tord_game_obj.dares_list[0]
        await bot.edit_message_text(text=f"{tord_game_obj.current_player_name}, {tord_game_obj.td_obj}", reply_markup=tord_kb.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)