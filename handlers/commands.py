from aiogram import types, Dispatcher
from config import bot, dp
import os

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f' hello {message.from_user.first_name} \n '
                                f'this is your telegram id - {message.from_user.id}')

@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'bots name is BotForLastTest \n'
                                f'this bot was created for past last test')

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(info, commands=['info'])