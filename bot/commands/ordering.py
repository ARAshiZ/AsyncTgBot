from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

from .keyboards import make_row_keyboard

available_food_names = ["Суши", "Спагетти", "Хачапури"]
available_food_sizes = ["Маленькую", "Среднюю", "Большую"]

class OrderFood(StatesGroup):
    choosing_food_name = State()
    choosing_food_size = State()

async def cmd_food(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите блюдо:",
        reply_markup=make_row_keyboard(available_food_names)
    )
    await state.set_state(OrderFood.choosing_food_name)

async def food_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_food=message.text.lower())
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите размер порции:",
        reply_markup=make_row_keyboard(available_food_sizes)
    )
    await state.set_state(OrderFood.choosing_food_size)

async def food_choosen_incorrectly(message: Message):
    await message.answer(
        text="Я не знаю такого блюда.\n\n"
             "Пожауйста, выберите одно из названий из списка ниже:",
        reply_markup=make_row_keyboard(available_food_names)
    )
async def food_size_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} порцию {user_data['chosen_food']}.\n"
             f"Попробуйте теперь заказать напитки /drinks",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()

async def food_size_chosen_incorrectly(message: Message):
    await message.answer(
        text="Я не знаю такого размера порции. \n\n"
             "Пожалуйста, выберите один из вариантов из списка ниже:",
        reply_markup=make_row_keyboard(available_food_sizes)
    )