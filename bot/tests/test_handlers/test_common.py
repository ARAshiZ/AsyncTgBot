import pytest
from unittest.mock import AsyncMock
from aiogram.fsm.context import FSMContext
from bot.commands.common import cmd_order

@pytest.mark.asyncio
async def test_common_order_handler():
    message = AsyncMock()
    state = FSMContext()
    await cmd_order(message=message, state=state)