import random
from aiogram import types
from bot.commands.constants import stickers


async def sticker_command(message: types.Message):
    sticker = random.choice(stickers)
    await message.answer_sticker(sticker)