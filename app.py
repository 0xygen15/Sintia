from aiogram import executor
import asyncio

from loader import dp

import handlers

async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()

if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    finally:
        asyncio.run(on_shutdown(dp))
        # await dp.storage.close()
        # await dp.storage.wait_closed()