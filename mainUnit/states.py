from aiogram.dispatcher.filters.state import State, StatesGroup

class DataBaseStates(StatesGroup):
    ready = State()


class PlayerStates(StatesGroup):
    ready_to_get_players_names = State()
    check_players_names = State()
    settings = State()
    mode = State()
    game = State()
    game_free = State()

class NieStates(StatesGroup):
    levels = State()
    game = State()

class ThreeOfFiveStates(StatesGroup):
    pass

class ThemesStates(StatesGroup):
    start = State()
    theme_choice = State()
    confirmation = State()
    game = State()

class AdsStates(StatesGroup):
    reading = State()
    checking = State()

class LangStates(StatesGroup):
    pending = State()

class Feedback(StatesGroup):
    pending = State()


class Advertise(StatesGroup):
    pending = State()
