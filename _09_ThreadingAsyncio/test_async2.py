import asyncio
import pytest_asyncio
import pytest
import asyncio


async def async_add(a, b):
    print("Starting async_add")
    await asyncio.sleep(5)  # Simulate an async operation
    print("Result From async_add", a + b)
    return a + b


async def async_sub(a, b):
    print("Starting async_sub")
    print("Result From async_sub", a - b)
    return a - b


# Basic Async test function
@pytest.mark.asyncio
async def test_async_add():
    result = await async_add(1, 2)
    assert result == 3


@pytest.mark.asyncio
async def test_async_sub():
    result = await async_sub(1, 2)
    assert result == -1
