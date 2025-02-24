import asyncio
from concurrent.futures import ThreadPoolExecutor

async def background_task(time: int):
    """ Simulate a long-running background task """
    await asyncio.sleep(time)  # Simulate async work
    print(f"Background task completed with data: {time}")

def run_asyncio_task(time: int):
    """ Wrapper to run the async function in a thread """
    asyncio.run(background_task(time))  # ✅ Runs async function inside a sync function


executor = ThreadPoolExecutor()

executor.submit(run_asyncio_task, 1)
executor.submit(run_asyncio_task, 4)
executor.submit(run_asyncio_task, 1)
executor.submit(run_asyncio_task, 3)
executor.submit(run_asyncio_task, 2)
print("Done")

