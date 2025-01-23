from idlelib.undo import Command
from typing import Optional

from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery


class CallBackDataObject(CallbackData, prefix='test'):
    command: str
    user_id: int
    text: Optional[str] = None
