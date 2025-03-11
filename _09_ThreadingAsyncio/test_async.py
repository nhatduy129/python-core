from demo.try_async import async_requests
import asyncio


def test_async():
    result = asyncio.run(async_requests.get("https://jsonplaceholder.typicode.com/posts"))
    assert result is not None
