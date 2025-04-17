from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
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
    keyboard_markup.button(
        text='Cоздать Reaply клавиатуру',
        callback_data='create_reaply1',
        user_id=message.from_user.id
    )
    keyboard_markup.button(
        text='Cоздать Reaply клавиатуру',
        callback_data='create_reaply2',
        user_id=message.from_user.id
    )
    await message.answer(welcome, reply_markup=keyboard_markup.as_markup())

async def create_reaply_keyboard1(call: CallbackQuery):
    button1 = KeyboardButton(text="1")
    button2 = KeyboardButton(text="2")
    button3 = KeyboardButton(text="3")
    button4 = KeyboardButton(text="4")
    button5 = KeyboardButton(text="5")
    button6 = KeyboardButton(text="6")
    button7 = KeyboardButton(text="7")
    button8 = KeyboardButton(text="8")
    button9 = KeyboardButton(text="9")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [button1, button2, button3],
            [button4, button5, button6],
            [button1, button2, button3, button4, button5, button6],
            [button4, button2],
            [button3, button2, button1],
            [button6, button9]
        ],
        resize_keyboard=True
    )
    await call.message.answer("Reaply клавиатура1", reply_markup=keyboard)


async def create_reaply_keyboard2(call: CallbackQuery):
    button1 = KeyboardButton(text="Первая кнопка!")
    button2 = KeyboardButton(text="Вторая кнопка")
    button3 = KeyboardButton(text="Кнопка 3")
    button4 = KeyboardButton(text="Кнопка 4")
    button5 = KeyboardButton(text="Кнопка 5")
    button6 = KeyboardButton(text="query=''")
    button7 = KeyboardButton(text="query='qwerty'")
    button8 = KeyboardButton(text="Inline в этом же чате")
    button9 = KeyboardButton(text="Уроки aiogram")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [button1],
            [button2],
            [button3, button4],
            [button5],
            [button3, button4, button5],
            [button6, button7],
            [button8],
            [button9]
        ],
        resize_keyboard=True
    )
    await call.message.answer("Reaply клавиатура2", reply_markup=keyboard)

async def bring_to_main(call: CallbackQuery):
    await call.message.edit_text(welcome, reply_markup=call.message.reply_markup)

