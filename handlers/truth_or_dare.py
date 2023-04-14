import logging
import typing

from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from mainUnit.engine import Engine
from mainUnit.keyboards import Keyboards, TordKeyboard
from mainUnit.players import Players
from mainUnit.states import PlayerStates

from local.lang import Texts


from loader import dp, bot

####

logging.basicConfig(level=logging.INFO)

engine = Engine()
player = Players()
# keyboards = Keyboards()
keyboards = TordKeyboard()

###

players_are_added = False
levels_are_chosen = False
mode_is_chosen = False

truth = ""
truth_index = 0
dare = ""
dare_index = 0
nie_index = 0


nie = ""
tord = ""
tord_t = True

current_player_name = ""
first_message_id: int
last_message_id: int

texts = Texts.truth_or_dare
###

@dp.message_handler(commands='truth_or_dare')
async def players_names(message: Message):
    global first_message_id
    first_message_id = message.message_id
    await PlayerStates.ready_to_get_players_names.set()
    await bot.send_message(chat_id=message.from_user.id, text=Texts.truth_or_dare["players names enter request"])
    logging.info("User is asked to enter names of players")



@dp.message_handler(state=PlayerStates.ready_to_get_players_names)
async def check_players_names(message: Message, state: FSMContext):
    await PlayerStates.check_players_names.set()
    player.add_player(player.list_of_players_names(data=message.text))
    names = ""
    for name in player.players_list:
        names += f"{name}\n"
    answer = f"""{Texts.truth_or_dare["check names"]}\n\n{names}\n{Texts.truth_or_dare["right?"]}"""
    if len(player.players_list) < 2:
        await state.finish()
        await bot.send_message(chat_id=message.from_user.id, text=f"{Texts.truth_or_dare['min2']} /truth_or_dare")
    else:
        await bot.send_message(chat_id=message.from_user.id, text=answer, reply_markup=keyboards.keyboard_players)
        logging.info(f"User has entered {player.players_list}")



@dp.callback_query_handler(keyboards.cb_players.filter(action='no'), state=PlayerStates.check_players_names)
async def players_no(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    player.players_list.clear()
    await query.answer()
    await PlayerStates.ready_to_get_players_names.set()
    await bot.send_message(chat_id=query.from_user.id, text=Texts.truth_or_dare["enter usernames"])
    logging.info("User reenters names")


@dp.callback_query_handler(keyboards.cb_players.filter(action='yes'), state=PlayerStates.check_players_names)
async def players_yes(query: CallbackQuery, callback_data: typing.Dict[str, str]):
    print(int(query.message.message_id))
    logging.info('Got this callback data: %r', callback_data)
    global players_are_added
    players_are_added = True
    await query.answer()
    await bot.send_message(chat_id=query.from_user.id, text=Texts.truth_or_dare["proceed to settings"])
    await PlayerStates.settings.set()
    await bot.send_message(text=texts["choose levels"],
                           chat_id=query.from_user.id,
                           reply_markup=keyboards.keyboard_level_all)
    logging.info(f"User has is offered to choose levels")



@dp.callback_query_handler(keyboards.cb_all_level.filter(action=['lifestyle', 'absurd', 'company', 'relations', 'awkward', 'ready']),
                           state=PlayerStates.settings)
async def settings(query: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):
    print(query.message.message_id)
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
            await bot.answer_callback_query(query.id, '🗿', True)
        else:
            await PlayerStates.mode.set()
            await bot.send_message(chat_id=query.from_user.id,
                                   text=Texts.truth_or_dare["mode"],
                                   reply_markup=keyboards.keyboard_mode)
    global levels_are_chosen
    if True in [keyboards.lifestyle_level, keyboards.absurd_level, keyboards.relations_level, keyboards.personal_level, keyboards.adult_level]:
        levels_are_chosen = True
    else:
        levels_are_chosen = False



@dp.callback_query_handler(keyboards.cb_mode.filter(action=['free', 'step']), state=PlayerStates.mode)
async def mode(query: CallbackQuery, state: FSMContext, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    answer = callback_data['action']
    global truth, dare, current_player_name, first_message_id, last_message_id
    last_message_id = query.message.message_id
    if answer == 'free':
        await PlayerStates.game_free.set()
        engine.set_levels(keyboards.lifestyle_level, keyboards.absurd_level, keyboards.relations_level, keyboards.personal_level, keyboards.adult_level)
        current_player_name = player.players_list[player.current_player_number]
        await bot.send_message(chat_id=query.from_user.id, text=f'{current_player_name}, {Texts.truth_or_dare["tord?"]}',
                               reply_markup=keyboards.keyboard_td)
        try:
            for mid in range(first_message_id, last_message_id+1):
                await bot.delete_message(chat_id=query.from_user.id, message_id=mid)
        except:
            pass

    elif answer == 'step':
        if levels_are_chosen == False and players_are_added == False:
            await bot.send_message(chat_id=query.from_user.id,
                                   text=Texts.truth_or_dare["players, level and mode!"])
        else:
            await PlayerStates.game.set()
            engine.set_levels(keyboards.lifestyle_level, keyboards.absurd_level, keyboards.relations_level, keyboards.personal_level, keyboards.adult_level)
            current_player_name = player.players_list[player.current_player_number]
            if player.truth_circle == True:
                truth = engine.shuffled_list(engine.t_all)[0]
                await bot.send_message(chat_id=query.from_user.id,
                                       text=f"{current_player_name}, {truth}",
                                       reply_markup=keyboards.keyboard_completed)
                try:
                    for mid in range(first_message_id, last_message_id+1):
                        await bot.delete_message(chat_id=query.from_user.id, message_id=mid)
                except:
                    pass
                logging.info(
                    f"Truth circle = {player.truth_circle}; "
                    f"Current player name: {current_player_name}; "
                    f"Truth: {truth}")
            elif player.truth_circle == False:
                dare = engine.shuffled_list(engine.d_all)[0]
                await bot.send_message(chat_id=query.from_user.id,
                                       text=f"{current_player_name}, {dare}",
                                       reply_markup=keyboards.keyboard_completed)
                try:
                    for mid in range(first_message_id, last_message_id+1):
                        await bot.delete_message(chat_id=query.from_user.id, message_id=mid)
                except:
                    pass
                logging.info(
                    f"Truth circle = {player.truth_circle};"
                    f"Current player name: {current_player_name};"
                    f"Dare: {dare};")



@dp.callback_query_handler(keyboards.cb_completed.filter(action=['completed', 'failed', 'over']),
                           state=PlayerStates.game)
async def game_step(query: CallbackQuery, state: FSMContext, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    answer = callback_data['action']
    message_id = query.message.message_id
    global truth, dare, current_player_name
    if answer == 'completed':
        player.next_player_number()
        player.circle_changer()

        if engine.out_of_objects(engine.t_all) == True or engine.out_of_objects(engine.d_all) == True:
            await state.finish()
            await query.answer()
            await bot.send_message(chat_id=query.from_user.id,
                                   text=f"{Texts.truth_or_dare['game over']} /truth_or_dare")

        if player.truth_circle == True:
            engine.t_all.remove(truth)
            current_player_name = player.players_list[player.current_player_number]
            truth = engine.shuffled_list(engine.t_all)[0]
            await bot.edit_message_text(chat_id=query.from_user.id,
                                   text=f"{current_player_name}, {truth}",
                                   reply_markup=keyboards.keyboard_completed,
                                   message_id = message_id)
            logging.info(
                f"\nTruth circle = {player.truth_circle}; "
                f"Current player name: {current_player_name}; "
                f"Current player number: {player.current_player_number};\n"
                f"Current q: {truth};\n"
                f"Length o lust: {len(engine.t_all)}")

        elif player.truth_circle == False:
            try:
                engine.d_all.remove(dare)
            except ValueError:
                pass
            current_player_name = player.players_list[player.current_player_number]
            dare = engine.shuffled_list(engine.d_all)[0]
            await bot.edit_message_text(chat_id=query.from_user.id,
                                   text=f"{current_player_name}, {dare}",
                                   reply_markup=keyboards.keyboard_completed,
                                   message_id = message_id)

            logging.info(
                f"\nTruth circle = {player.truth_circle}; "
                f"Current player name: {current_player_name}; "
                f"Current player number: {player.current_player_number};\n"
                f"Current q: {dare};\n"
                f"Length o lust: {len(engine.d_all)}")

    elif answer == 'failed':
        if player.fail_check(current_player_name) == True:
            await bot.answer_callback_query(query.id,
                                            f'{current_player_name}, {Texts.truth_or_dare["penalty"]}',
                                            True)
        player.score[current_player_name]['p'] += 1
        if player.truth_circle == True:
            truth = engine.shuffled_list(engine.t_all)[0]
            await bot.edit_message_text(chat_id=query.from_user.id,
                                   text=f"{current_player_name}, {truth}",
                                   reply_markup=keyboards.keyboard_completed,
                                   message_id=query.message.message_id)
        elif player.truth_circle == False:
            dare = engine.shuffled_list(engine.d_all)[0]
            await bot.edit_message_text(chat_id=query.from_user.id,
                                        text=f"{current_player_name}, {dare}",
                                        reply_markup=keyboards.keyboard_completed,
                                        message_id=query.message.message_id)

    elif answer == "over":
        await state.finish()
        await query.answer()
        player.players_list.clear()
        await bot.send_message(chat_id=query.from_user.id,
                               text=f"{Texts.truth_or_dare['game over']} /truth_or_dare")
        await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)



@dp.callback_query_handler(keyboards.cb_td.filter(action=['truth', 'dare', 'end']),
                           state=PlayerStates.game_free)
async def game_free(query: CallbackQuery, state: FSMContext, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    answer = callback_data['action']
    global tord, tord_t, current_player_name
    current_player_name = player.players_list[player.current_player_number]
    if answer == 'truth':
        tord_t = True
        tord = engine.shuffled_list(engine.t_all)[0]
        await bot.edit_message_text(text=f"{current_player_name}, {tord}", reply_markup=keyboards.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)
    elif answer == 'dare':
        tord_t = False
        tord = engine.shuffled_list(engine.d_all)[0]
        await bot.edit_message_text(text=f"{current_player_name}, {tord}", reply_markup=keyboards.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)
    elif answer == 'end':
        player.players_list.clear()
        await state.finish()
        await bot.send_message(chat_id=query.from_user.id, text=Texts.truth_or_dare["game over"])
        await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)



@dp.callback_query_handler(keyboards.cb_completed_f.filter(action=['completed_f', 'failed_f']),
                           state=PlayerStates.game_free)
async def game_free_c(query: CallbackQuery, state: FSMContext, callback_data: typing.Dict[str, str]):
    logging.info('Got this callback data: %r', callback_data)
    answer = callback_data['action']
    global tord, tord_t, current_player_name
    if answer == 'completed_f':
        if tord_t == True:
            engine.t_all.remove(tord)
        elif tord_t == False:
            engine.d_all.remove(tord)
        player.next_player_number()
        current_player_name = player.players_list[player.current_player_number]
        await bot.edit_message_text(chat_id=query.from_user.id, text=f'{current_player_name}, {Texts.truth_or_dare["tord?"]}',
                               reply_markup=keyboards.keyboard_td, message_id=query.message.message_id)

    elif answer == 'failed_f':
        if player.fail_check(current_player_name) == True:
            await bot.answer_callback_query(query.id,
                                            f'{current_player_name}, {Texts.truth_or_dare["penalty"]}',
                                            True)
        player.score[current_player_name]['p'] += 1
        if tord_t == True:
            tord = engine.shuffled_list(engine.t_all)[0]
        elif tord_t == False:
            tord = engine.shuffled_list(engine.d_all)[0]
        await bot.edit_message_text(text=f"{current_player_name}, {tord}", reply_markup=keyboards.keyboard_completed_f,
                                    message_id=query.message.message_id, chat_id=query.from_user.id)