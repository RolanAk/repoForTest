import sqlite3
from db import queries

db = sqlite3.connect('db/products.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена!')
    cursor.execute(queries.CREATE_TABLE_TABLE)

async def sql_insert_product(name, category, size, price, article, photo):
    cursor.execute(queries.INSERT_PRODUCTS, (
        name, category, size, price, article, photo
    ))
    db.commit()