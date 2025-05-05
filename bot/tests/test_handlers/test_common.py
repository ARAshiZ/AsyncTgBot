import pytest
from unittest.mock import AsyncMock

import pytest_asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove
from sqlalchemy.orm import defer

from bot.commands import food_chosen, OrderFood, available_food_sizes
from bot.commands.common import cmd_order
from bot.commands.keyboards import make_row_keyboard
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


@pytest.mark.asyncio
async def test_food_chosen_command():
    message = AsyncMock(text="суши")
    state = AsyncMock()
    await food_chosen(message=message, state=state)
    state.update_data.assert_called_once_with(chosen_food="суши")
    message.answer.assert_called_once_with(
        text="Спасибо. Теперь, пожалуйста, выберите размер порции:",
        reply_markup=make_row_keyboard(available_food_sizes)
    )
    state.set_state.assert_called_once_with(OrderFood.choosing_food_size)

@pytest.mark.asyncio
async def test_start_text():
    message = AsyncMock(text='/start')

    assert message.text == '/start'