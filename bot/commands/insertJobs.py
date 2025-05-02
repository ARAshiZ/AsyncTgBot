import datetime
from random import setstate
from aiogram import types
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from bot.database.services.dbservice import DatabaseService


class JobsForm(StatesGroup):
    waiting_for_title = State()
    waiting_for_payment = State()
    waiting_for_high_education = State()
    result_state = State()

async def insert_jobs(message: types.Message, service: DatabaseService, state: FSMContext):
    await message.answer('Что бы создать вакансию необходимо ввести название:')
    await state.set_state(JobsForm.waiting_for_title)

async def process_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(JobsForm.waiting_for_payment)
    await message.answer('Введите зарплату:')

async def process_payment(message: types.Message, state: FSMContext):
    await state.update_data(payment=round(float(message.text), 2))
    await state.set_state(JobsForm.waiting_for_high_education)
    await message.answer('Нужно ли высшее образование? (да/нет):')

async def process_high_education(message: types.Message, state: FSMContext, service: DatabaseService):
    if message.text.lower() in ['да', 'yes']:
        await state.update_data(high_edu=True)
        await process_result(message, state, service)
    elif message.text.lower() in ['нет', 'no']:
        await state.update_data(high_edu=False)
        await process_result(message, state, service)
    else:
        await message.answer('Введите да или нет(yes or no).')



async def process_result(message: types.Message, state: FSMContext, service: DatabaseService):
    try:
        user_data = await state.get_data()
        job_title = user_data['title']
        job_payment = user_data['payment']
        higher_education = user_data['high_edu']
        await service.insert_job(job_title, job_payment, higher_education)
        await message.answer('Вакансия добавлена!')
        await state.clear()
    except:
        await message.answer('Не удалось добавить вакансию :(')


