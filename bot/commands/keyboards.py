from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from typing import List

from aiogram.utils.keyboard import ReplyKeyboardBuilder


def make_row_keyboard(items: List[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)

keyboard_builder= ReplyKeyboardBuilder()


keyboard_builder.button(
    text='Помощь',
    callback_data='help',
)

keyboard_builder.add(
KeyboardButton(
    text='Стикер',
    callback_data='sticker',
))
keyboard_builder.add(
    KeyboardButton(
    text='В меню',
    callback_data='back',
))
