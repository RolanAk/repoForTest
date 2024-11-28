from aiogram import types, Dispatcher, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import staff, Admins, bot

class FsmZakaz(StatesGroup):

    article = State()
    size = State()
    count = State()
    number = State()


async def start_fsmzakaz(message: types.Message):
    await FsmZakaz.article.set()
    await message.answer(text='введите артикл товара')

async def load_article(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['article'] = message.text

    await message.answer("Введите размер товара: ")
    await FsmZakaz.next()


async def load_size(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer("Введите количество товара: ")
    await FsmZakaz.next()

async def load_count(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['count'] = message.text

    await message.answer("Введите свой номер: ")
    await FsmZakaz.next()


async def load_number(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text

        await bot.send_message(chat_id='1268007497',
                               text=f'заполненный товар: \n'
                                    f'article - {data["article"]}\n'
                                    f'size - {data["size"]}\n'
                                    f'count - {data["count"]}\n'
                                    f'number - {data["number"]}')

    await FsmZakaz.next()

def register_handler_fsm_zakaz(dp: Dispatcher):
    dp.register_message_handler(start_fsmzakaz, commands=['zakaz'])
    dp.register_message_handler(load_size, state=FsmZakaz.size)
    dp.register_message_handler(load_article, state=FsmZakaz.article)
    dp.register_message_handler(load_count, state=FsmZakaz.count)
    dp.register_message_handler(load_number, state=FsmZakaz.number)