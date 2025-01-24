from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.commands.constants import welcome


async def create_menu(message: types.Message):
    keyboard_markup = InlineKeyboardBuilder()

    keyboard_markup.button(
        text='Помощь',
        callback_data='help',
        user_id=message.from_user.id
    )
    keyboard_markup.button(
        text='Стикер',
        callback_data='sticker',
        user_id=message.from_user.id
    )
    keyboard_markup.button(
        text='В меню',
        callback_data='back',
        user_id=message.from_user.id
    )
    await message.answer(welcome, reply_markup=keyboard_markup.as_markup())

async def bring_to_main(call: CallbackQuery):
    await call.message.edit_text(welcome, reply_markup=call.message.reply_markup)