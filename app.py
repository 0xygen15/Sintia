from aiogram import executor

from loader import dp

from local.lang import Texts

import handlers

if __name__ == '__main__':
    # Texts.load_localisation()
    executor.start_polling(dp, skip_updates=True)