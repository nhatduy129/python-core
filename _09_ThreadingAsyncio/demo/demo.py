import asyncio
import threading


async def my_task():
    print("my_task")
    await asyncio.sleep(1)
    print("my_task done")

async_run = lambda: asyncio.run(my_task())
thread = threading.Thread(target=async_run)
thread.start()
thread.join()