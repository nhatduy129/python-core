import asyncio
import time


task_registry = {}

async def my_task(task_id, duration):
    """Runs only the latest task with the same task_id"""
    if task_id in task_registry:  
        task_registry[task_id].cancel()  # Cancel previous task
        print(f"Previous task {task_id} canceled.")

    async def run():
        print(f"Task {task_id} is running...")
        await asyncio.sleep(duration)
        print(f"Task {task_id} finished.")

    task_registry[task_id] = asyncio.create_task(run())  # Store the new task
    return task_registry[task_id]

async def main():
    await asyncio.gather(
        my_task("task_1", 5),
        my_task("task_1", 3),  # This should cancel the previous "task_1"
        my_task("task_2", 4),  # Runs separately
    )

asyncio.run(main())
print("ok")
time.sleep(6)

# def background_task():
#     asyncio.run(main())
#     print("ok")

# thread1 = threading.Thread(target=background_task)
# thread2 = threading.Thread(target=background_task)
# thread1.start()
# # thread2.start()






