import datetime
from random import setstate
from aiogram import types
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.services.dbservice import DatabaseService


class AboutForm(StatesGroup):
    waiting_for_model_title = State()
    waiting_for_model_info = State()
    result_state = State()

async def insert_about(message: types.Message, service: DatabaseService, state: FSMContext):
    await message.answer('Что бы добавить информацию о таблицах нужно ввести название:')
    tables = await service.get_table_names()
    response = "Список таблиц:\n\n"
    for table in tables:
        response += f"{table}\n"
    await message.answer(response)
    await state.set_state(AboutForm.waiting_for_model_title)

async def process_info_title(message: types.Message, service: DatabaseService, state: FSMContext):
    tables = await service.get_table_names()
    if message.text in tables:
        await state.update_data(title=message.text)
        await state.set_state(AboutForm.waiting_for_model_info)
        await message.answer('Введите информацию о таблице:')
    else:
        await message.answer('Такой таблицы не существует!')

async def process_info(message: types.Message,service: DatabaseService, state: FSMContext):
    await state.update_data(info=message.text)
    await process_result(message, state, service)

async def process_result(message: types.Message, state: FSMContext, service: DatabaseService):
    try:
        user_data = await state.get_data()
        table_title = user_data['title']
        information = user_data['info']
        date = datetime.date.today()
        await service.insert_about(table_title, information, date)
        await message.answer('Информация добавлена!')
        await state.clear()
    except:
        await message.answer('Не удалось добавить информацию :(')


