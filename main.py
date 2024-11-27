import logging
from aiogram import executor, types
from config import dp
from handlers import commands, fsm_zapis
from db import db_main

commands.register_commands(dp)
fsm_zapis.register_handler_fsm_zapis(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, allowed_updates=['callback'])

