import logging
from aiogram import executor, types
from config import dp, Admins, bot
from handlers import commands, fsm_zapis, send_products, fsm_zakaz
from db import db_main

commands.register_commands(dp)
fsm_zapis.register_handler_fsm_zapis(dp)
fsm_zakaz.register_handler_fsm_zakaz(dp)
send_products.register_handler_send_products(dp)

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включен!')

        await db_main.sql_create()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, allowed_updates=['callback'],on_startup=on_startup)

