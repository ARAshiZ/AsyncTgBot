import asyncio
import pytest
import pytest_asyncio
from aiogram import Dispatcher

@pytest_asyncio.fixture
async def dispatcher():
    dp = Dispatcher()
    await dp.emit_startup()
    try:
        yield dp
    finally:
        await dp.emit_shutdown()

@pytest.fixture
def event_loop():
    return asyncio.get_event_loop()