import random
from aiogram import types

from bot.commands import bring_to_main
from bot.commands.constants import stickers, welcome
import asyncio


async def sticker_command(message: types.Message):
    sticker = random.choice(stickers)
    await message.answer_sticker(sticker)

async def call_sticker(call: types.CallbackQuery):
    sticker = random.choice(stickers)
    await call.message.edit_text('Отправлен стикер на 5 секунд. Наслаждайтесь!)', reply_markup=call.message.reply_markup)
    sent_sticker = await call.message.answer_sticker(sticker)
    await asyncio.sleep(2)
    await sent_sticker.delete()
    await bring_to_main(call)

