import asyncio
import psutil
import os

async def fake_io_task(task_id):
    """ Giả lập một tác vụ I/O như đọc ghi file, truy vấn DB """
    await asyncio.sleep(2)  # Giả lập thời gian chờ
    return f"Task {task_id} completed"

async def main():
    num_tasks = 100000  # Số task chạy đồng thời

    # Đo RAM trước khi chạy task
    process = psutil.Process(os.getpid())
    ram_before = process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB

    # Tạo danh sách task
    tasks = [fake_io_task(i) for i in range(num_tasks)]
    
    # Chạy tất cả các task đồng thời
    results = await asyncio.gather(*tasks)

    # Đo RAM sau khi chạy task
    ram_after = process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB

    print(f"RAM before: {ram_before:.2f} MB")
    print(f"RAM after: {ram_after:.2f} MB")
    print(f"RAM used: {ram_after - ram_before:.2f} MB")

# Chạy asyncio event loop
asyncio.run(main())
