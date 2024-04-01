from aiogram import executor
import asyncio

# import subprocess
# subprocess.run(['sh', 'venv/bin/activate'])

from loader import dp

import handlers

from mainUnit.database import Database

async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()

if __name__ == '__main__':
    try:
        Database.create_database_if_not_exists()
        executor.start_polling(dp, skip_updates=True)
    finally:
        asyncio.run(on_shutdown(dp))
        # await dp.storage.close()
        # await dp.storage.wait_closed()