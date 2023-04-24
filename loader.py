from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from mainUnit.config import API_TOKEN


bot = Bot(token=API_TOKEN)
# storage = MemoryStorage()
storage = RedisStorage2(host="localhost", port=6379, db=1)
dp = Dispatcher(bot, storage=storage)