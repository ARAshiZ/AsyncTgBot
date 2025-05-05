import pytest
from unittest.mock import AsyncMock

import pytest_asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove

from bot.commands.common import cmd_order
from bot.tests.mocked_bot import MockedBot
from bot.tests.utils import TEST_USER, TEST_USER_CHAT

@pytest_asyncio.fixture(scope='session')
async def storage():
    tmp_storage = MemoryStorage()
    try:
        yield tmp_storage
    finally:
        await tmp_storage.close()

@pytest.fixture
def bot():
    return MockedBot()

@pytest.mark.asyncio
async def test_common_order_handler(storage, bot):
    message = AsyncMock()
    state = FSMContext(
        storage=storage,
        key=StorageKey(bot_id=bot.id, user_id=TEST_USER.id, chat_id=TEST_USER_CHAT.id)
    )
    await cmd_order(message=message, state=state)

    assert await state.get_state() is None

    message.answer.assert_called_with(
        text="Выберите, что хотите заказать: "
             "блюда (/food) или напитки (/drinks)",
        reply_markup=ReplyKeyboardRemove()
    )