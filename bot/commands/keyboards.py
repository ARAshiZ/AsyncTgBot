from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from typing import List

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def make_row_keyboard(items: List[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)

keyboard_builder= InlineKeyboardBuilder()


keyboard_builder.button(
    text='Помощь',
    callback_data='help',
)
keyboard_builder.button(
    text='Стикер',
    callback_data='sticker',
)
keyboard_builder.button(
    text='В меню',
    callback_data='back',
)
keyboard_builder.button(
    text='keyb1',
    callback_data='create_reaply1'
)
keyboard_builder.button(
    text='keyb2',
    callback_data='create_reaply2'
)
