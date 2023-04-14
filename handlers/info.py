import typing

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from mainUnit.engine import Users
from mainUnit.keyboards import ConfigKeyboard
from mainUnit.states import LangStates

from local.lang import Texts


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

themes_description = {
                        "school": """Тема «школа» посвящена воспоминаниям и опыту, связанным с образованием.
                                 Будь то первый день в школе, любимый учитель или школьная поездка, у каждого есть своя уникальная
                                 история, чтобы поделиться о временах в школе. Эти вопросы идеально подходят для ностальгирующего
                                 путешествия по переулку памяти и возможности узнать больше об образовании ваших друзей
                                 и их опыте.""",

                        "work": """Работа является важной частью жизни многих людей и может формировать их мировоззрение и личную жизнь.
                                 Эти 30 гипотетических вопросов о работе предназначены для изучения
                                 выборов, с которым люди могут столкнуться в своей карьере, и дать представление об их
                                 приоритетах и цели, а также немало поведать о разных курьезных ситуациях""",
                        "travel": """Путешествие может быть захватывающим и обогащающим опытом, которое расширяет наши границы
                                 и знакомит нас с новыми культурами и образами жизни. Будь то изучение нового города, отдых на
                                 пляже или приключение, путешествие предлагает бесконечные возможности. Однако оно также может
                                 прийти со своим собственным набором проблем и трудных решений. Эти вопросы о путешествии
                                 предназначены для побуждения к размышлению и обсуждению различных аспектов путешествия,
                                 от планирования и подготовки до неожиданных препятствий и культурных различий.""",
                        "worldview": """Мировоззрение - это то, как мы видим и понимаем окружающий нас мир, основанный на нашем
                                опыте, убеждениях, ценностях и культурном происхождении. Это формирует то, как мы думаем, чувствуем и действуем,
                                и влияет на наш выбор и решения в жизни. Эти вопросы направлены на изучение
                                ваших взглядов на различные аспекты жизни, такие как мораль, политика, религия и этика,
                                и как как вы ориентируетесь в сложных ситуациях и делаете трудный выбор. Приготовьтесь поразмыслить над своими
                                глубочайшими убеждениями и участвуйте в наводящих на размышления беседах со своими друзьями.""",
                        "social media": """Социальные сети стали неотъемлемой частью современной жизни, и трудно
                                представить мир без них. От поддержания связи с друзьями и семьей до обмена нашими
                                мыслями и мнениями с миром социальные сети изменили то, как мы общаемся.
                                Эти вопросы о социальных сетях позволят понять, как люди их используют, какое влияние они оказывают на их
                                жизни и как они ориентируются в сложностях онлайн-отношений.""",
                        "art": """Вопросы, связанные с искусством, могут вдохновлять на творчество и воображение, а также могут обеспечить
                                окно в эстетические предпочтения человека и его художественную восприимчивость. Они также могут раскрыть
                                культурное происхождение человека и его понимание различных форм искусства, стилей и течений.""",
                        "relations": """Вопросы, связанные с романтическими отношениями, исследуют динамику и эмоции
                                вовлечения в романтические связи между людьми. Эти вопросы могут охватывать широкий круг
                                тем, таких как личные ценности, стили общения, совместимость и ожидания.
                                Они также могут углубиться в более специфические аспекты романтических отношений, такие как близость,
                                доверие, обязательства и разрешение конфликтов. Ответы на эти вопросы могут раскрыть личность человека,
                                прошлый опыт, текущие отношения и будущие цели в контексте романтических
                                отношений.""",
                        "memes": """Мемы - популярная форма интернет-культуры, которая в последние годы захватила мир штурмом
                                . Они могут быть забавными, привлекательными и часто служат социальным комментарием. Вопросы
                                , связанные с мемами, могут многое рассказать о чувстве юмора человека, его интересах и их
                                знание текущих событий и популярной культуры. Будь то обмен любимым мемом или
                                создание нового, эти вопросы обязательно вызовут интересную беседу.""",
                        "religion": """Религия - сложная и личная тема, которая влияет на убеждения,
                                ценности и поведение людей. Это может обеспечить общность, но также может
                                привести к конфликтам и разделению. Эти вопросы о религии предназначены для изучения
                                различных аспектов веры и духовности, от личных убеждений до культурных традиций,
                                а также способствовать пониманию между людьми с различным происхождением
                                . Независимо от того, являетесь ли вы верующим или атеистом, эти вопросы могут бросить вызов.
                                Вы должны поразмыслить над своим собственным мировоззрением и вступить в содержательные беседы с другими.""",
                        "memories": """Детские воспоминания часто могут быть одними из самых дорогих моментов нашей жизни.
                                Эти вопросы помогут вызвать ностальгию и вернуть приятные воспоминания о летних лагерях,
                                семейных каникулах, школьных днях и многом другом. Приготовьтесь совершить путешествие по переулку памяти!""",
                        "if": """Вопросы, связанные с гипотетическими вариантами юмора, разработаны таким образом, чтобы быть занимательными и
                                заставляющий задуматься. Они часто представляют участникам юмористические, но трудные гипотетические
                                сценарии и заставляют их принимать трудное решение. Эти вопросы могут раскрыть
                                личность человека, его чувство юмора и стиль принятия решений. Они также могут быть забавным способом
                                познакомиться с новыми людьми.""",
                        "video games": """Видеоигры были популярной формой развлечения на протяжении десятилетий, и они
                                продолжают развиваться и захватывать воображение игроков по всему миру. Независимо от того, являетесь ли вы
                                геймером, здесь найдется интерес для каждого. Эти вопросы будут
                                исследовать различные аспекты видеоигр, от любимых названий и персонажей до игровых
                                привычек и мнений об индустрии. Будьте готовы повысить уровень своих знаний и поделиться своей
                                страстью ко всему игровому!""",
                        "education": """Эти вопросы предназначены для того, чтобы вызвать дискуссии об образовании и обучении.
                                Они затрагивают самые разные темы, такие как методы преподавания, цель образования и
                                ценность различных видов знаний. Цель вопросов - стимулировать критическое мышление о
                                образование и его роль в формировании личности и общества в целом.""",
                        "fashion": """Мода - это постоянно развивающаяся индустрия, которая отражает меняющиеся тенденции и
                                стили общества. Являетесь ли вы fashion-личностью или нет, у всех нас есть свое мнение о том, что выглядит
                                хорошо, а что нет. Мода может быть веселым и творческим способом самовыражения, но она
                                также может быть источником стресса и замешательства. Эти вопросы, связанные с модой, предназначены для
                                интересной беседы и исследования различных аспектов этого увлекательного
                                мира. От обсуждения последних тенденций моды до обмена личным выбором одежды, эти
                                вопросы побудят вас выразить свое уникальное чувство стиля и узнать больше о
                                предпочтениях окружающих вас людей в моде.""",
                        "hard choice": """Эти вопросы призваны бросить вызов вашим навыкам принятия решений и
                                раскрыть ваши личные ценности и убеждения. Они часто представляют сложные сценарии, в которых вам
                                приходится выбирать между двумя или более одинаково привлекательными вариантами, заставляя вас взвешивать
                                все "за" и "против" и принимать трудные решения. Цель состоит в том, чтобы увидеть, как вы подходите к трудным ситуациям
                                и какие факторы влияют на ваш выбор, такие как эмпатия, рациональность или личные интересы."""
}

# texts = Texts.info

@dp.message_handler(commands='info')
async def info(message: Message):
    await bot.send_message(text=Texts.info["info"], chat_id=message.from_user.id, parse_mode='HTML')


@dp.message_handler(commands='start')
async def start(message: Message, state: FSMContext):
    await state.finish()
    user_chat_data = {
        'chat_id': message.chat.id,
        'chat_type': message.chat.type,
        'username': message.from_user.username,
        'fName': message.from_user.first_name,
        'lName': message.from_user.last_name,
        'user_id': message.from_user.id,
        'language_code': message.from_user.language_code,
        'is_bot': message.from_user.is_bot
    }
    Users.create_table() # create db if not created
    Users.create(user_chat_data) #add user data to db if bot added yet
    Texts.lang_code = Users.get_user_lang_code(message.from_user.id)
    Texts.load_localisation(Texts.lang_code) #load localisation files
    await bot.send_message(text=Texts.info["start"], chat_id=message.from_user.id, parse_mode='HTML')


@dp.message_handler(commands='refresh', state='*')
async def start(message: Message, state: FSMContext):
    await state.finish()
    await bot.send_message(text=Texts.info["refresh"], chat_id=message.from_user.id, parse_mode='HTML')

@dp.message_handler(commands="language")
async def language(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text="Choose language/Выбери язык", reply_markup=ConfigKeyboard.kb_lang)
    await LangStates.pending.set()

@dp.callback_query_handler(ConfigKeyboard.cb_lang.filter(action=['en', 'de', 'fr', 'es', 'sr', 'ru', 'uk']),
                           state=LangStates.pending)
async def choose_language(query: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):
    answer = callback_data['action']
    if answer == 'en':
        Users.change_user_lang_code('en', query.message.from_user.id)
        Texts.lang_code = Users.get_user_lang_code(query.message.from_user.id)
        Texts.load_localisation(Texts.lang_code)
        await bot.edit_message_text(text="English language chosen as a default. Have a nice game!",
                                    chat_id=query.message.chat.id, message_id=query.message.message_id,
                                    reply_markup=None)
        await state.finish()
    elif answer == 'de':
        Users.change_user_lang_code('de', query.message.from_user.id)
        Texts.lang_code = Users.get_user_lang_code(query.message.from_user.id)
        Texts.load_localisation(Texts.lang_code)
        await bot.edit_message_text(text="Standardmäßig ist die deutsche Sprache gewählt. Haben Sie ein schönes Spiel!",
                                    chat_id=query.message.chat.id, message_id=query.message.message_id,
                                    reply_markup=None)
        await state.finish()
    elif answer == 'fr':
        Users.change_user_lang_code('fr', query.message.from_user.id)
        Texts.lang_code = Users.get_user_lang_code(query.message.from_user.id)
        Texts.load_localisation(Texts.lang_code)
        await bot.edit_message_text(text="Langue française choisie par défaut. Bon jeu !", chat_id=query.message.chat.id,
                                    message_id=query.message.message_id,
                                    reply_markup=None)
        await state.finish()
    elif answer == 'es':
        Users.change_user_lang_code('es', query.message.from_user.id)
        Texts.lang_code = Users.get_user_lang_code(query.message.from_user.id)
        Texts.load_localisation(Texts.lang_code)
        await bot.edit_message_text(text="Idioma español elegido por defecto. ¡Que tengas un buen juego!",
                                    chat_id=query.message.chat.id, message_id=query.message.message_id,
                                    reply_markup=None)
        await state.finish()
    elif answer == 'sr':
        Users.change_user_lang_code('sr', query.message.from_user.id)
        Texts.lang_code = Users.get_user_lang_code(query.message.from_user.id)
        Texts.load_localisation(Texts.lang_code)
        await bot.edit_message_text(text="Српски језик изабран као подразумевани. Угодна игра!",
                                    chat_id=query.message.chat.id, message_id=query.message.message_id,
                                    reply_markup=None)
        await state.finish()
    elif answer == 'ru':
        Users.change_user_lang_code('ru', query.message.from_user.id)
        Texts.lang_code = Users.get_user_lang_code(query.message.from_user.id)
        Texts.load_localisation(Texts.lang_code)
        await bot.edit_message_text(text="Русский язык выбран по умолчанию. Приятной игры!",
                                    chat_id=query.message.chat.id, message_id=query.message.message_id,
                                    reply_markup=None)
        await state.finish()
    elif answer == 'uk':
        Users.change_user_lang_code('uk', query.message.from_user.id)
        Texts.lang_code = Users.get_user_lang_code(query.message.from_user.id)
        Texts.load_localisation(Texts.lang_code)
        await bot.edit_message_text(text="За замовчуванням вибрано українську мову. Гарної гри!",
                                    chat_id=query.message.chat.id, message_id=query.message.message_id,
                                    reply_markup=None)
        await state.finish()
