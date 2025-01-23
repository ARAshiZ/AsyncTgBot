from idlelib.undo import Command

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.commands.constants import welcome
from bot.commands.states_callback import CallBackDataObject
from bot.commands.help import call_help
from bot.commands.sticker import call_sticker

async def show_menu(message: types.Message):
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
    await message.answer(welcome, reply_markup=keyboard_markup.as_markup())

