from aiogram import executor

from loader import dp

import handlers

if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()