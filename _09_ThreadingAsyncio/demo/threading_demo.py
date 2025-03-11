import threading
import time

task_locks = {}

def get_task_lock(task_id):
    if task_id not in task_locks:
        task_locks[task_id] = threading.Lock()
    return task_locks[task_id]

def my_task(task_id, duration):
    lock = get_task_lock(task_id)
    with lock:  # Đảm bảo chỉ có 1 task cùng task_id chạy tại một thời điểm
        print(f"Task {task_id} is running...")
        time.sleep(duration)  # Giả lập công việc mất thời gian
        print(f"Task {task_id} finished.")

def run_task(task_id, duration):
    thread = threading.Thread(target=my_task, args=(task_id, duration))
    thread.start()
    return thread

# Chạy các task
threads = []
threads.append(run_task("task_1", 5))
threads.append(run_task("task_1", 3))  # Sẽ đợi task_1 trước đó xong rồi mới chạy
threads.append(run_task("task_2", 4))  # Chạy song song vì task_id khác
threads.append(run_task("task_3", 2))  # Chạy song song vì task_id khác

# Đợi tất cả các task hoàn thành
for t in threads:
    t.join()

print("All tasks completed.")
