from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot


text_info = """
Инструкция:

<b>1. "Я никогда не ...":</b> /never_i_ever

Понадобится ведущий🦊. Он или она будет озвучивать всем игрокам "я никогда не...", которые бот сгенерирует в чат.

Например: <i>Я никогда</i> не одевался в костюм Дарта Вейдера и расхаживал в нём по городу. 

Собственно, игрок который имел радость рассекать в костюме Дарта по городу загибает один палец на руке. 
Когда у игрока накопилось 5 загнутых пальцев, то он, сообщая об этом ведущему, должен выбрать Правду или Действие. 

Ведущий договаривается с участниками о порядке выбора Правды и Действия. 
Могут быть круги Правды, круги Действия, круги Правды и Действия или же по выбору игроков.

<b>2. "Правда или действие":</b> /truth_or_dare

Есть два режима игры: свободный и поочередный. Свободный - вы сами выбираете когда правда, а когда действие.
Поочередный - бот будет присылать поочередно правду и действие.

<b>3. "Три из пяти":</b> /three_of_five

Игроку будет преложено пять категорий вопросов, действий и "я никогда не". Из каждой категории игрок обязан на своё 
усмотрение ответить на 3 из 5 вопросов, выполнить 3 из 5 действий. В случае с "я никогда не" другие игроки должны угадать,
что из этого игрок делал, а что нет.

<b>Описание уровней:</b>

О жизни: вопросы мировоззрения, жизни, а также действия.
Абсурдные: аналогично предыдущему, но больше юмора.
Для компании: уже не холодно, но ещё не жарко.
Отношения: буквально написанному.
Неловкие: неловкие вопросы и действия, однако с уважением личных границ.
"""

start_text = """
Привет! Вот инструкции и список игр. Хорошо тебе провести время!

<b>/info</b> - Инструкции и описание. Рекомендовано к прочтению перед игрой.

<b>/truth_or_dare</b> - Играть в "Правда или Действие"
<b>/never_i_ever</b> - Играть в "Я никогда не"
<b>/three_of_five</b> - Играть в "Три из пяти"

<b>/refresh</b> - Остановить игру/Перезагрузить бота/Выйти в любой момент

Запустить игру можно также из кнопки "Меню". 
"""

refresh_text = """
Бот перезагружен.

<b>/info</b> - Инструкции и описание. Рекомендовано к прочтению перед игрой.

<b>/truth_or_dare</b> - Играть в "Правда или Действие"
<b>/never_i_ever</b> - Играть в "Я никогда не"
<b>/three_of_five</b> - Играть в "Три из пяти"

<b>/refresh</b> - Остановить игру/Перезагрузить бота/Выйти в любой момент

Запустить игру можно также из кнопки "Меню". 
"""

theme_school = """test desc"""
theme_work = """test desc"""
theme_travel = """test desc"""
theme_worldview = """test desc"""
theme_social_media = """test desc"""
theme_art = """test desc"""
theme_relations = """test desc"""
theme_memes = """test desc"""
theme_religion = """test desc"""
theme_memories = """test desc"""
theme_the_if = """test desc"""
theme_videogames = """test desc"""
theme_education = """test desc"""
theme_fashion = """test desc"""
theme_hard_choice = """test desc"""


@dp.message_handler(commands='info')
async def info(message: Message):
    await bot.send_message(text=text_info, chat_id=message.from_user.id, parse_mode='HTML')


@dp.message_handler(commands='start')
async def start(message: Message, state: FSMContext):
    await state.finish()
    await bot.send_message(text=start_text, chat_id=message.from_user.id, parse_mode='HTML')


@dp.message_handler(commands='refresh', state='*')
async def start(message: Message, state: FSMContext):
    await state.finish()
    await bot.send_message(text=refresh_text, chat_id=message.from_user.id, parse_mode='HTML')