import asyncio

# Dictionary to store running tasks
task_registry = {}

async def my_task(task_id, duration):
    """Runs only the latest task with the same task_id"""
    if task_id in task_registry:  
        task_registry[task_id].cancel()  # Cancel previous task
        print(f"Previous task {task_id} canceled.")
        try:
            await task_registry[task_id]  # Ensure cancellation completes
        except asyncio.CancelledError:
            print(f"Task {task_id} was properly cancelled.")

    async def run():
        print(f"Task {task_id} is running...")
        await asyncio.sleep(duration)
        print(f"Task {task_id} finished.")

    task_registry[task_id] = asyncio.create_task(run())  # Store the new task

async def main():
    await asyncio.gather(
        my_task("task_1", 5),
        my_task("task_1", 3),  # This should cancel the previous "task_1"
        my_task("task_2", 4),  # Runs separately
    )

    # Ensure all remaining tasks are completed
    await asyncio.gather(*task_registry.values())

asyncio.run(main())
