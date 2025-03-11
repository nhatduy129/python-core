import threading
import time

# Dictionary chứa lock cho từng task_id

class TaskManager:
    _instance = None
    _task_locks = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def _get_task_lock(self, task_id):
        if task_id not in self._task_locks:
            self._task_locks[task_id] = threading.Lock()
        return self._task_locks[task_id]

    def my_task(self, task_id, duration):
        lock = self._get_task_lock(task_id)
        with lock:  # Đảm bảo chỉ có 1 task cùng task_id chạy tại một thời điểm
            print(f"Task {task_id} is running...")
            time.sleep(duration)  # Giả lập công việc mất thời gian
            print(f"Task {task_id} finished.")

    def run_task(self, task_id, duration):
        thread = threading.Thread(target=self.my_task, args=(task_id, duration))
        thread.start()
        return thread

# a = TaskManager()
# b = TaskManager()

# print(a is b)
# a.task_locks["task_1"] = threading.Lock()
# print(a.task_locks)
# print(b.task_locks)

# Chạy các task
threads = []
threads.append(TaskManager().run_task("task_1", 5))
threads.append(TaskManager().run_task("task_1", 3))  # Sẽ đợi task_1 trước đó xong rồi mới chạy
threads.append(TaskManager().run_task("task_2", 4))  # Chạy song song vì task_id khác
threads.append(TaskManager().run_task("task_3", 2))  # Chạy song song vì task_id khác
print("ok")

# Đợi tất cả các task hoàn thành
for t in threads:
    t.join()

print("All tasks completed.")
