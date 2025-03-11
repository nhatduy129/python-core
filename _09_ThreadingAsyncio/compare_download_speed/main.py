import requests
from concurrent.futures import ThreadPoolExecutor
import time
import asyncio
import aiohttp
import ssl
import certifi


MAX_TASK = 100


def download_task():
    response = requests.get("https://www.google.com")
    return response.content

def one_thread():
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=1) as executor:
        for i in range(MAX_TASK):
            executor.submit(download_task)
    end_time = time.time()
    print(f"One thread takes: {end_time - start_time} seconds")

def five_threads_simultaneously():
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(MAX_TASK):
            executor.submit(download_task)
    end_time = time.time()
    print(f"5 threads take: {end_time - start_time} seconds")
    
def ten_threads_simultaneously():
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(MAX_TASK):
            executor.submit(download_task)
    end_time = time.time()
    print(f"10 threads take: {end_time - start_time} seconds")
    
def twenty_threads_simultaneously():
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(MAX_TASK):
            executor.submit(download_task)
    end_time = time.time()
    print(f"20 threads take: {end_time - start_time} seconds")
    
def forty_threads_simultaneously():
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=40) as executor:
        for i in range(MAX_TASK):
            executor.submit(download_task)
    end_time = time.time()
    print(f"40 threads take: {end_time - start_time} seconds")

async def fetch(session, url):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with session.get(url, ssl=ssl_context) as response:
        result = await response.text()
        return result
    
async def download_task_for_asyncio():
    async with aiohttp.ClientSession() as session:
        reponse = await fetch(session, "https://www.google.com")
        return reponse
    
async def main_asyncio():
    tasks = [download_task_for_asyncio() for _ in range(MAX_TASK)]
    await asyncio.gather(*tasks)
    
def one_thread_with_asyncio():
    start_time = time.time()
    asyncio.run(main_asyncio())
    end_time = time.time()
    print(f"One thread with asyncio takes: {end_time - start_time} seconds")

if __name__ == "__main__":
    print("Start one thread")
    one_thread()
    print("Start 5 threads simultaneously")
    five_threads_simultaneously()
    print("Start 10 threads simultaneously")
    ten_threads_simultaneously()
    print("Start 20 threads simultaneously")
    twenty_threads_simultaneously()
    print("Start 40 threads simultaneously")
    forty_threads_simultaneously()
    print("Start one thread with asyncio")
    one_thread_with_asyncio()