import json
import os
import tkinter as tk

import aiogram

#
# with open("old/dare.json", "r", encoding="utf8") as tf:
#     data_old = json.load(tf)
#
#
# lk = 6
# mk = 110
# hk = 79
# index = 0
#
# with open("data_d.txt", "r", encoding="utf8") as f:
#     data_new = [q for q in f]
#
# def text():
#     global index, data_new
#     q = data_new[index]
#     return q
#
# def w():
#     with open(file="old/dare.json", mode="w", encoding="utf8") as wf:
#         json.dump(data_old, wf, ensure_ascii=False, indent=6)
#     l, m, h = len(data_old["low"]), len(data_old["middle"]), len(data_old["high"])
#     print(f"L={l}, M={m}, H={h}")
#     with open("data_d.txt", "w", encoding="utf8") as ttxt:
#         for item in data_new:
#             ttxt.write(item)
#     print(f"remain: {len(data_new)}")
#
#
# def l1():
#     global lk
#     data_old["low"][len(data_old["low"]) + 1] = text()
#     lk += 1
#     data_new.remove(text())
#     w()
#     next_text()
#
# def m1():
#     global mk
#     data_old["middle"][len(data_old["middle"]) + 1] = text()
#     mk += 1
#     data_new.remove(text())
#     w()
#     next_text()
#
# def h1():
#     global hk
#     data_old["high"][len(data_old["high"]) + 1] = text()
#     hk += 1
#     data_new.remove(text())
#     w()
#     next_text()
#
#
# window = tk.Tk()
#
# window.title("Расфасовка")
# window.minsize(400, 100)
# window.config(padx=50, pady=50)
#
# text_ = tk.Label(text=text())
#
# def next_text():
#     global index, data_new
#     index += 1
#     text_.config(text=text())
#
#
# low_button = tk.Button(text="Общие", command=l1)
# middle_button = tk.Button(text="Узнать лучше", command=m1)
# high_button = tk.Button(text="Личные", command=h1)
#
# text_.grid(column=1, row=0)
# low_button.grid(column=0, row=1)
# middle_button.grid(column=1, row=1)
# high_button.grid(column=2, row=1)
#
# tk.mainloop()

"d"
# with open("database/truth.json", "r", encoding="utf8") as ft:
#     data = json.load(ft)
#     lt = [v for k, v in data["low"].items()]
#     mt = [v for k, v in data["middle"].items()]
#     ht = [v for k, v in data["high"].items()]
#
# with open("database/dare.json", "r", encoding="utf8") as fd:
#     data = json.load(fd)
#     ld = [v for k, v in data["low"].items()]
#     md = [v for k, v in data["middle"].items()]
#     hd = [v for k, v in data["high"].items()]
#
# with open("database/truth.json", "w", encoding="utf8") as ftw:
#     data = {"low": {}, "middle": {}, "high": {}}
#     lk = 1
#     mk = 1
#     hk = 1
#     for item1 in lt:
#         i1 = item1.replace("❓ ", "")
#         i2 = i1.replace("\n", "")
#         data["low"][lk] = i2
#         lk += 1
#     for item2 in mt:
#         i1 = item2.replace("❓ ", "")
#         i2 = i1.replace("\n", "")
#         data["middle"][mk] = i2
#         mk += 1
#     for item3 in ht:
#         i1 = item3.replace("❓ ", "")
#         i2 = i1.replace("\n", "")
#         data["high"][hk] = i2
#         hk += 1
#     json.dump(data, ftw, ensure_ascii=False, indent=6)
#
# with open("database/dare.json", "w", encoding="utf8") as ftd:
#     data = {"low": {}, "middle": {}, "high": {}}
#     lkd = 1
#     mkd = 1
#     hkd = 1
#     for item1 in ld:
#         i1 = item1.replace("❗️", "")
#         i2 = i1.replace("\n", "")
#         data["low"][lkd] = i2
#         lkd += 1
#     for item2 in md:
#         i1 = item2.replace("❗️", "")
#         i2 = i1.replace("\n", "")
#         data["middle"][mkd] = i2
#         mkd += 1
#     for item3 in hd:
#         i1 = item3.replace("❗️", "")
#         i2 = i1.replace("\n", "")
#         data["high"][hkd] = i2
#         hkd += 1
#     json.dump(data, ftd, ensure_ascii=False, indent=6)

"""w"""
# with open("database/never.txt", "r", encoding="utf8") as f:
#     data_old = [q for q in f]
#     data_new = []
#     for q in data_old:
#         if q == "\n":
#             pass
#         else:
#             n = ''.join([i for i in q if not i.isdigit()])
#             n1 = n.replace(" ", "", 0)
#             n2 = n1.replace("\n", "")
#             n3 = n2.replace(". ", "")
#             data_new.append(n3)
#
# with open("database/never_cleared.txt", "w", encoding="utf8") as f1:
#     for q in list(dict.fromkeys(data_new)):
#         f1.write(f"{q}\n")

"""n"""
# with open("database/never_cleared.txt", "r", encoding="utf8") as f:
#     data_raw = [n for n in f]
#
# with open("database/never.json", "r", encoding="utf8") as fo:
#     data_old = json.load(fo)
#
# index = 0
#
# def text():
#     global index, data_raw
#     q = data_raw[index]
#     return q
#
# def w():
#     with open(file="database/never_.json", mode="w", encoding="utf8") as wf:
#         json.dump(data_old, wf, ensure_ascii=False, indent=6)
#     l, m, h = len(data_old["low"]), len(data_old["middle"]), len(data_old["high"])
#     print(f"L={l}, M={m}, H={h}")
#     with open("database/never_cleared.txt", mode="w", encoding="utf8") as txt:
#         for item in data_raw:
#             txt.write(item)
#     print(f"Remain: {len(data_raw)}")
#
#
# def l1():
#     data_old["low"][len(data_old["low"]) + 1] = text()
#     data_raw.remove(text())
#     w()
#     next_text()
#
# def m1():
#     data_old["middle"][len(data_old["middle"]) + 1] = text()
#     data_raw.remove(text())
#     w()
#     next_text()
#
# def h1():
#     data_old["high"][len(data_old["high"]) + 1] = text()
#     data_raw.remove(text())
#     w()
#     next_text()
#
# def no():
#     data_raw.remove(text())
#     next_text()
#
#
# window = tk.Tk()
#
# window.title("Расфасовка")
# window.minsize(400, 100)
# window.config(padx=50, pady=50)
#
# text_ = tk.Label(text=text())
#
# def next_text():
#     global index, data_new
#     index += 1
#     text_.config(text=text())
#
#
# low_button = tk.Button(text="Общие", command=l1)
# middle_button = tk.Button(text="Узнать лучше", command=m1)
# high_button = tk.Button(text="Личные", command=h1)
# no_button = tk.Button(text="Пропустить", command=no)
#
# text_.grid(column=1, row=0)
# low_button.grid(column=0, row=1)
# middle_button.grid(column=1, row=1)
# high_button.grid(column=2, row=1)
# no_button.grid(column=1, row=2)
#
# tk.mainloop()

"""tdnew"""


# with open("database/dare.json", "r", encoding="utf8") as f:
#     do_json = json.load(f)
#     dol = []
#     for k, v in do_json["low"].items():
#         dol.append(v)
#     for k, v in do_json["middle"].items():
#         dol.append(v)
#     for k, v in do_json["high"].items():
#         dol.append(v)
#
# with open("database/all_d.txt", "w", encoding="utf8") as af:
#     for i in dol:
#         af.write(i)
#         af.write("\n")

# with open("database/never_cleared.txt", "r", encoding="utf8") as af:
#     dol = []
#     for i in af:
#         dol.append(i)
#
# def remove_and_rewrite(i):
#     dol.remove(i)
#     with open("database/never_cleared.txt", "w", encoding="utf8") as aa:
#         for item in dol:
#             aa.write(item)
#
# def get_length(a, b, c):
#     return len(a), len(b), len(c)
#
#
# with open("database/never.json", "r", encoding="utf8") as tr:
#     new_data = json.load(tr)
#
# def store():
#     with open("database/never.json", "w", encoding="utf8") as tn:
#         json.dump(new_data, tn, ensure_ascii=False, indent=6)
#
# i = 0
#
# while len(dol) >= 0:
#     print("#" * 50)
#     print("'1' for LIFESTYLE, '2' for ABSURD, '3' for RELATIONS, '4' for PERSONAL, '5' for ADULT, '6' to remove")
#     a = input(f"\n{dol[i]}\n")
#     r = dol[i]
#     if a == "1":
#         new_data["lifestyle"][len(new_data["lifestyle"]) + 1] = dol[i]
#         remove_and_rewrite(r)
#         store()
#         print(f"Left: {len(dol)}")
#         print(f'Current: L: {len(new_data["lifestyle"])}, A: {len(new_data["absurd"])}, R: {len(new_data["relations"])},'
#               f' P: {len(new_data["personal"])}, Ad: {len(new_data["adult"])}')
#         i += 1
#
#     elif a == "2":
#         new_data["absurd"][len(new_data["absurd"]) + 1] = dol[i]
#         remove_and_rewrite(r)
#         store()
#         print(f"Left: {len(dol)}")
#         print(
#             f'Current: L: {len(new_data["lifestyle"])}, A: {len(new_data["absurd"])}, R: {len(new_data["relations"])},'
#             f' P: {len(new_data["personal"])}, Ad: {len(new_data["adult"])}')
#         i += 1
#     elif a == "3":
#         new_data["relations"][len(new_data["relations"]) + 1] = dol[i]
#         remove_and_rewrite(r)
#         store()
#         print(f"Left: {len(dol)}")
#         print(
#             f'Current: L: {len(new_data["lifestyle"])}, A: {len(new_data["absurd"])}, R: {len(new_data["relations"])},'
#             f' P: {len(new_data["personal"])}, Ad: {len(new_data["adult"])}')
#         i += 1
#     elif a == "4":
#         new_data["personal"][len(new_data["personal"]) + 1] = dol[i]
#         remove_and_rewrite(r)
#         store()
#         print(f"Left: {len(dol)}")
#         print(
#             f'Current: L: {len(new_data["lifestyle"])}, A: {len(new_data["absurd"])}, R: {len(new_data["relations"])},'
#             f' P: {len(new_data["personal"])}, Ad: {len(new_data["adult"])}')
#         i += 1
#     elif a == "5":
#         new_data["adult"][len(new_data["adult"]) + 1] = dol[i]
#         remove_and_rewrite(r)
#         store()
#         print(f"Left: {len(dol)}")
#         print(
#             f'Current: L: {len(new_data["lifestyle"])}, A: {len(new_data["absurd"])}, R: {len(new_data["relations"])},'
#             f' P: {len(new_data["personal"])}, Ad: {len(new_data["adult"])}')
#         i += 1
#     elif a == "6":
#         remove_and_rewrite(r)
#         store()
#         i += 1

# def data(filepath):
#     with open(filepath, 'r', encoding='utf8') as f:
#         return [i for i in json.load(f)]

# class DataManagement:
#     ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#     database_folder_path = "\database2"
#     truth_file = r"\truth.json"
#     dare_file = r"\dare.json"
#     never_file = r"\never.json"
#     truth_target_file = r"\truth.csv"
#     dare_target_file = r"\dare.csv"
#     never_target_file = r"\never.csv"
#     def __init__(self):
#         pass
#
#     def json_file_to_dict(self, filename):
#         with open(file=f"{DataManagement.ROOT_DIR}{DataManagement.database_folder_path}{filename}",
#                   mode="r", encoding='utf8') as f:
#             data = json.load(f)
#             return data
#
#     def csv_to_dict(self, filename):
#         with open(file=f"{DataManagement.ROOT_DIR}{DataManagement.database_folder_path}{filename}",
#                   mode="r", encoding='utf8') as f:
#             pass

# def aligner(source_file):
#     with open(source_file, 'r', encoding='utf8') as source_file:
#         source_json = json.load(source_file)
#         target_json = {}
#         index = 1
#         for level, data in source_json.items():
#             target_json[level] = {}
#             current_dict = target_json[level]
#             for key, value in data.items():
#                 index_str = str(index)
#                 current_dict[index_str] = value
#                 index += 1
#             index = 1
#         return target_json
#
# # print(json.dumps(aligner("./database2/truth.json"), indent=4, ensure_ascii=False))
# def writer(f):
#     with open(f, "r+", encoding='utf8') as ff:
#         json_file = json.dumps(aligner(f), indent=4, ensure_ascii=False)
#         ff.write("")
#         ff.write(json_file)
#
#
# file_paths = ["./database2/truth.json",
#               "./database2/dare.json",
#               "./database2/never.json"]
#
# for file in file_paths:
#     writer(file)
# #365, 332, 322


# text_info = """
# Инструкция:
#
# <b>1. "Я никогда не ...":</b> /never_i_ever
#
# Понадобится ведущий🦊. Он или она будет озвучивать всем игрокам "я никогда не...", которые бот сгенерирует в чат.
#
# Например: <i>Я никогда</i> не одевался в костюм Дарта Вейдера и расхаживал в нём по городу.
#
# Собственно, игрок который имел радость рассекать в костюме Дарта по городу загибает один палец на руке.
# Когда у игрока накопилось 5 загнутых пальцев, то он, сообщая об этом ведущему, должен выбрать Правду или Действие.
#
# Ведущий договаривается с участниками о порядке выбора Правды и Действия.
# Могут быть круги Правды, круги Действия, круги Правды и Действия или же по выбору игроков.
#
# <b>2. "Правда или действие":</b> /truth_or_dare
#
# Есть два режима игры: свободный и поочередный. Свободный - вы сами выбираете когда правда, а когда действие.
# Поочередный - бот будет присылать поочередно правду и действие.
#
# <b>3. "Три из пяти":</b> /three_of_five
#
# Игроку будет преложено пять категорий вопросов, действий и "я никогда не". Из каждой категории игрок обязан на своё
# усмотрение ответить на 3 из 5 вопросов, выполнить 3 из 5 действий. В случае с "я никогда не" другие игроки должны угадать,
# что из этого игрок делал, а что нет.
#
# <b>Описание уровней:</b>
#
# О жизни: вопросы мировоззрения, жизни, а также действия.
# Абсурдные: аналогично предыдущему, но больше юмора.
# Для компании: уже не холодно, но ещё не жарко.
# Отношения: буквально написанному.
# Неловкие: неловкие вопросы и действия, однако с уважением личных границ.
# """
#
# start_text = """
# Привет! Вот инструкции и список игр. Хорошо тебе провести время!
#
# <b>/info</b> - Инструкции и описание. Рекомендовано к прочтению перед игрой.
#
# <b>/truth_or_dare</b> - Играть в "Правда или Действие"
# <b>/never_i_ever</b> - Играть в "Я никогда не"
# <b>/three_of_five</b> - Играть в "Три из пяти"
#
# <b>/refresh</b> - Остановить игру/Перезагрузить бота/Выйти в любой момент
#
# Запустить игру можно также из кнопки "Меню".
# """
#
# refresh_text = """
# Бот перезагружен.
#
# <b>/info</b> - Инструкции и описание. Рекомендовано к прочтению перед игрой.
#
# <b>/truth_or_dare</b> - Играть в "Правда или Действие"
# <b>/never_i_ever</b> - Играть в "Я никогда не"
# <b>/three_of_five</b> - Играть в "Три из пяти"
#
# <b>/refresh</b> - Остановить игру/Перезагрузить бота/Выйти в любой момент
#
# Запустить игру можно также из кнопки "Меню".
# """
#
# themes_description = {
#                         "school": """Тема «школа» посвящена воспоминаниям и опыту, связанным с образованием.
#                                  Будь то первый день в школе, любимый учитель или школьная поездка, у каждого есть своя уникальная
#                                  история, чтобы поделиться о временах в школе. Эти вопросы идеально подходят для ностальгирующего
#                                  путешествия по переулку памяти и возможности узнать больше об образовании ваших друзей
#                                  и их опыте.""",
#
#                         "work": """Работа является важной частью жизни многих людей и может формировать их мировоззрение и личную жизнь.
#                                  Эти 30 гипотетических вопросов о работе предназначены для изучения
#                                  выборов, с которым люди могут столкнуться в своей карьере, и дать представление об их
#                                  приоритетах и цели, а также немало поведать о разных курьезных ситуациях""",
#                         "travel": """Путешествие может быть захватывающим и обогащающим опытом, которое расширяет наши границы
#                                  и знакомит нас с новыми культурами и образами жизни. Будь то изучение нового города, отдых на
#                                  пляже или приключение, путешествие предлагает бесконечные возможности. Однако оно также может
#                                  прийти со своим собственным набором проблем и трудных решений. Эти вопросы о путешествии
#                                  предназначены для побуждения к размышлению и обсуждению различных аспектов путешествия,
#                                  от планирования и подготовки до неожиданных препятствий и культурных различий.""",
#                         "worldview": """Мировоззрение - это то, как мы видим и понимаем окружающий нас мир, основанный на нашем
#                                 опыте, убеждениях, ценностях и культурном происхождении. Это формирует то, как мы думаем, чувствуем и действуем,
#                                 и влияет на наш выбор и решения в жизни. Эти вопросы направлены на изучение
#                                 ваших взглядов на различные аспекты жизни, такие как мораль, политика, религия и этика,
#                                 и как как вы ориентируетесь в сложных ситуациях и делаете трудный выбор. Приготовьтесь поразмыслить над своими
#                                 глубочайшими убеждениями и участвуйте в наводящих на размышления беседах со своими друзьями.""",
#                         "social media": """Социальные сети стали неотъемлемой частью современной жизни, и трудно
#                                 представить мир без них. От поддержания связи с друзьями и семьей до обмена нашими
#                                 мыслями и мнениями с миром социальные сети изменили то, как мы общаемся.
#                                 Эти вопросы о социальных сетях позволят понять, как люди их используют, какое влияние они оказывают на их
#                                 жизни и как они ориентируются в сложностях онлайн-отношений.""",
#                         "art": """Вопросы, связанные с искусством, могут вдохновлять на творчество и воображение, а также могут обеспечить
#                                 окно в эстетические предпочтения человека и его художественную восприимчивость. Они также могут раскрыть
#                                 культурное происхождение человека и его понимание различных форм искусства, стилей и течений.""",
#                         "relations": """Вопросы, связанные с романтическими отношениями, исследуют динамику и эмоции
#                                 вовлечения в романтические связи между людьми. Эти вопросы могут охватывать широкий круг
#                                 тем, таких как личные ценности, стили общения, совместимость и ожидания.
#                                 Они также могут углубиться в более специфические аспекты романтических отношений, такие как близость,
#                                 доверие, обязательства и разрешение конфликтов. Ответы на эти вопросы могут раскрыть личность человека,
#                                 прошлый опыт, текущие отношения и будущие цели в контексте романтических
#                                 отношений.""",
#                         "memes": """Мемы - популярная форма интернет-культуры, которая в последние годы захватила мир штурмом
#                                 . Они могут быть забавными, привлекательными и часто служат социальным комментарием. Вопросы
#                                 , связанные с мемами, могут многое рассказать о чувстве юмора человека, его интересах и их
#                                 знание текущих событий и популярной культуры. Будь то обмен любимым мемом или
#                                 создание нового, эти вопросы обязательно вызовут интересную беседу.""",
#                         "religion": """Религия - сложная и личная тема, которая влияет на убеждения,
#                                 ценности и поведение людей. Это может обеспечить общность, но также может
#                                 привести к конфликтам и разделению. Эти вопросы о религии предназначены для изучения
#                                 различных аспектов веры и духовности, от личных убеждений до культурных традиций,
#                                 а также способствовать пониманию между людьми с различным происхождением
#                                 . Независимо от того, являетесь ли вы верующим или атеистом, эти вопросы могут бросить вызов.
#                                 Вы должны поразмыслить над своим собственным мировоззрением и вступить в содержательные беседы с другими.""",
#                         "memories": """Детские воспоминания часто могут быть одними из самых дорогих моментов нашей жизни.
#                                 Эти вопросы помогут вызвать ностальгию и вернуть приятные воспоминания о летних лагерях,
#                                 семейных каникулах, школьных днях и многом другом. Приготовьтесь совершить путешествие по переулку памяти!""",
#                         "if": """Вопросы, связанные с гипотетическими вариантами юмора, разработаны таким образом, чтобы быть занимательными и
#                                 заставляющий задуматься. Они часто представляют участникам юмористические, но трудные гипотетические
#                                 сценарии и заставляют их принимать трудное решение. Эти вопросы могут раскрыть
#                                 личность человека, его чувство юмора и стиль принятия решений. Они также могут быть забавным способом
#                                 познакомиться с новыми людьми.""",
#                         "video games": """Видеоигры были популярной формой развлечения на протяжении десятилетий, и они
#                                 продолжают развиваться и захватывать воображение игроков по всему миру. Независимо от того, являетесь ли вы
#                                 геймером, здесь найдется интерес для каждого. Эти вопросы будут
#                                 исследовать различные аспекты видеоигр, от любимых названий и персонажей до игровых
#                                 привычек и мнений об индустрии. Будьте готовы повысить уровень своих знаний и поделиться своей
#                                 страстью ко всему игровому!""",
#                         "education": """Эти вопросы предназначены для того, чтобы вызвать дискуссии об образовании и обучении.
#                                 Они затрагивают самые разные темы, такие как методы преподавания, цель образования и
#                                 ценность различных видов знаний. Цель вопросов - стимулировать критическое мышление о
#                                 образование и его роль в формировании личности и общества в целом.""",
#                         "fashion": """Мода - это постоянно развивающаяся индустрия, которая отражает меняющиеся тенденции и
#                                 стили общества. Являетесь ли вы fashion-личностью или нет, у всех нас есть свое мнение о том, что выглядит
#                                 хорошо, а что нет. Мода может быть веселым и творческим способом самовыражения, но она
#                                 также может быть источником стресса и замешательства. Эти вопросы, связанные с модой, предназначены для
#                                 интересной беседы и исследования различных аспектов этого увлекательного
#                                 мира. От обсуждения последних тенденций моды до обмена личным выбором одежды, эти
#                                 вопросы побудят вас выразить свое уникальное чувство стиля и узнать больше о
#                                 предпочтениях окружающих вас людей в моде.""",
#                         "hard choice": """Эти вопросы призваны бросить вызов вашим навыкам принятия решений и
#                                 раскрыть ваши личные ценности и убеждения. Они часто представляют сложные сценарии, в которых вам
#                                 приходится выбирать между двумя или более одинаково привлекательными вариантами, заставляя вас взвешивать
#                                 все "за" и "против" и принимать трудные решения. Цель состоит в том, чтобы увидеть, как вы подходите к трудным ситуациям
#                                 и какие факторы влияют на ваш выбор, такие как эмпатия, рациональность или личные интересы."""
# }