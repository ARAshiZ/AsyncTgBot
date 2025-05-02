import datetime
from random import setstate
from aiogram import types
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from bot.database.services.dbservice import DatabaseService

class SubscribeForm(StatesGroup):
    waiting_for_sub_title = State()
    waiting_for_sub_term = State()
    waiting_for_sub_price = State()
    result_state = State()

async def insert_subscribe(message: types.Message, state: FSMContext):
    await message.answer('Что бы создать подписку необходимо ввести название:')
    await state.set_state(SubscribeForm.waiting_for_sub_title)

async def process_sub_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(SubscribeForm.waiting_for_sub_term)
    await message.answer('Введите срок окончания подписки:')

async def process_sub_date(message: types.Message, state: FSMContext):
    date_str = message.text
    date = date_check(date_str)
    await state.update_data(term=date.date())
    await state.set_state(SubscribeForm.waiting_for_sub_price)
    await message.answer('Введите стоимость подписки:')

async def process_sub_price(message: types.Message, state: FSMContext, service: DatabaseService):
    await state.update_data(price=round(float(message.text), 2))
    await process_result(message, state, service)

async def process_result(message: types.Message, state: FSMContext, service: DatabaseService):
    try:
        user_data = await state.get_data()
        sub_title = user_data['title']
        sub_term = user_data['term']
        sub_price = user_data['price']
        await service.insert_subscribe(sub_title, sub_term, sub_price)
        await message.answer('Подписка добавлена!')
        await state.clear()
    except:
        await message.answer('Не удалось добавить подписку :(')

def date_check(date_str: str) -> datetime:
    try:
        return datetime.datetime.strptime(date_str, "%Y.%m.%d")
    except ValueError:
        return None