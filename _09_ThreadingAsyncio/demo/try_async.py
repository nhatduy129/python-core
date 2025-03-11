import asyncio
import aiohttp
import ssl
import certifi


class AsyncRequests:
    def __init__(self):
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())

    async def get(self, url: str, params: dict = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, ssl=self.ssl_context) as response:
                return await response.json()

    async def post(self, url: str, data: dict = None):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, ssl=self.ssl_context) as response:
                return await response.json()

    async def get_image(self, url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=self.ssl_context) as response:
                return await response.content.read()

async_requests = AsyncRequests()


result = asyncio.run(async_requests.get_image("https://scontent.xx.fbcdn.net/v/t39.30808-1/419943864_6948969795221113_4478095634414679166_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=79bf43&_nc_ohc=CBHTgWr3J0AQ7kNvgF5lOv_&_nc_oc=AdhDdQNOJbqJ1dkufMRd9FqY85EKiM-1fqXJSvaY7jNcqyZYB09oA2LJ6W4GBFwCrvo&_nc_zt=24&_nc_ht=scontent.xx&edm=AGaHXAAEAAAA&_nc_gid=AcBt4v2pVccHkN5idrz3BRI&oh=00_AYFR7cAm9VbCwRzhFSQQPAGghSw1Z1HyogQOP2tD1o0FaA&oe=67D181D4"))
print(result)
