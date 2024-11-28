import products
from aiogram import types, Dispatcher
import sqlite3
from db import queries
from db.db_main import cursor


async def send_products(message: types.Message):

    conn = sqlite3.connect('db/products.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    products_str = "\n".join([str(products) for product in products])
    await message.answer(products_str)
    conn.close()

def register_handler_send_products(dp: Dispatcher):
    dp.register_message_handler(send_products, commands=['products'])