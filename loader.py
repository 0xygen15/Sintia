from typing import Dict

from aiogram import Bot, Dispatcher
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from mainUnit.config import API_TOKEN
from mainUnit.users import Users

from local.lang import Texts

bot = Bot(token=API_TOKEN)
# storage = MemoryStorage()
storage = RedisStorage2(host="localhost", port=6379, db=1)
dp = Dispatcher(bot, storage=storage)

#Localisation objects
loc_ru, loc_uk, loc_sr, loc_en, loc_de, loc_fr, loc_es = Texts("ru"), Texts("uk"), Texts("sr"), Texts("en"), Texts("de"), Texts("fr"), Texts("es")

#dict with user object where are all thew user's objects are stored
user_objects: Dict[str, Users]= {}

#dict with loc objects for access from any place of project
loc_objects: Dict[str, Texts] = {
    "ru": loc_ru,
    "uk": loc_uk,
    "sr": loc_sr,
    "en": loc_en,
    "de": loc_de,
    "fr": loc_fr,
    "es": loc_es
}
