from typing import Dict

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
# from redis import asyncio as aioredis

from mainUnit.config import API_TOKEN
from mainUnit.users import Users

from local.lang import Texts

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
# storage = RedisStorage2(host="localhost", port=6379, db=1, pool_size=10)
dp = Dispatcher(bot, storage=storage)


