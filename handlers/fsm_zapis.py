from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from db import db_main

class FsmRecord(StatesGroup):

    name = State()
    category = State()
    size = State()
    price = State()
    article = State()
    photo = State()
    submit = State()

async def start_fsm_record(message: types.Message):
    await FsmRecord.name.set()
    await message.answer(text='введите название товара')


async def load_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer("Введите категорию для товара: ")
    await FsmRecord.next()

async def load_category(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer("введите размер товара: ")
    await FsmRecord.next()

async def load_size(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer("введите цену товара: ")
    await FsmRecord.next()

async def load_price(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer("введите артикул товара: ")
    await FsmRecord.next()

async def load_article(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['article'] = message.text

    await message.answer("введите фото товара: ")
    await FsmRecord.next()

async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['photo'],
                                caption=f"Заполненный товар: \n"
                                         f"Название - {data['name']}\n"
                                         f"категория - {data['category']}\n"
                                         f"размер - {data['size']}\n"
                                         f"цена - {data['price']}\n"
                                         f"артикл - {data['article']}\n")

    await FsmRecord.next()

async def submit(message: types.Message, state=FSMContext):

        async with state.proxy() as data:
            await db_main.sql_insert_product(
                name=data['name'],
                category=data['category'],
                size=data['size'],
                price=data['price'],
                article=data['article'],
                photo=data['photo'],
            )


def register_handler_fsm_zapis(dp: Dispatcher):
    dp.register_message_handler(start_fsm_record, commands=['fsm'])
    dp.register_message_handler(load_name, state=FsmRecord.name)
    dp.register_message_handler(load_category, state=FsmRecord.category)
    dp.register_message_handler(load_size, state=FsmRecord.size)
    dp.register_message_handler(load_price, state=FsmRecord.price)
    dp.register_message_handler(load_article, state=FsmRecord.article)
    dp.register_message_handler(load_photo, state=FsmRecord.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FsmRecord.submit)
