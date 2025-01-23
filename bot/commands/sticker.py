import random
from aiogram import types
from bot.commands.constants import stickers


async def sticker_command(message: types.Message):
    sticker = random.choice(stickers)
    await message.answer_sticker(sticker)

async def call_sticker(call: types.CallbackQuery):
    sticker = random.choice(stickers)
    await call.message.edit_text('Отправлен стикер', reply_markup=call.message.reply_markup)
    await call.message.answer_sticker(sticker)
