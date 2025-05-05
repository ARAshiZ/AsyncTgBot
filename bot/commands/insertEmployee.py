import datetime
from random import setstate

from aiogram import types
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.services.dbservice import DatabaseService


class EmployeeForm(StatesGroup):
    waiting_for_user_id = State()
    waiting_for_offer = State()


async def insert_employee(message: types.Message, service: DatabaseService, state: FSMContext):
    await message.answer('Что бы создать сотрудника, необходимо выбрать пользователя:')
    users = await service.exists_users()
    response = "Список пользователей:\n\n"
    for user in users:
        response += (
            f"ID: {user.user_id}\n"
            f"Имя: {user.user_name}\n"
        )
    await message.answer(response)
    await state.set_state(EmployeeForm.waiting_for_user_id)


async def process_user_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Это не число! Пожалуйста, введите цифру.")
        return

    await state.update_data(user_id=int(message.text))
    await state.set_state(EmployeeForm.waiting_for_offer)
    await message.answer('Введите должность сотрудника:')


async def process_offer(message: types.Message, state: FSMContext, service: DatabaseService):
    try:
        user_data = await state.get_data()
        user_id = user_data['user_id']
        offer = message.text
        date = datetime.date.today()
        await service.insert_employee(user_id, offer, date)
        await message.answer('Сотрудник добавлен!')
        await state.clear()
    except:
        await message.answer('Не удалось добавить сотрудника :(')


