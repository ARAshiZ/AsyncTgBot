import pytest
from unittest.mock import AsyncMock

from bot.commands.keyboards import keyboard_builder
from bot.commands.start import create_menu

@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    await create_menu(message)

    message.answer.assert_called_with(
        'Привет! Выбери действие:',
        reply_markup=keyboard_builder.as_markup()
    )