import threading
import time
import psutil
import os

def task():
    time.sleep(5)  # Simulating a long-running task

# Creating 1000 threads
threads = [threading.Thread(target=task) for _ in range(4000)]

# Start all threads
for t in threads:
    t.start()

# Get memory usage
process = psutil.Process(os.getpid())
print(f"Memory Usage: {process.memory_info().rss / (1024 * 1024)} MB")

# Wait for all threads to finish
for t in threads:
    t.join()
