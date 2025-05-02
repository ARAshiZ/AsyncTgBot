from email import message_from_string

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

async def cmd_order(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Выберите, что хотите заказать: "
             "блюда (/food) или напитки (/drinks)",
        reply_markup=ReplyKeyboardRemove()
    )

async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({})
    await message.answer(
        text="Нечего отменять",
        reply_markup=ReplyKeyboardRemove()
    )

async def cmd_cancel(messsage: Message, state: FSMContext):
    await state.clear()
    await messsage.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )
