from django.core.management.base import BaseCommand
from asyncdatabase.models import Student
import time
import threading
import asyncio  


class Command(BaseCommand):
    help = "In ra thông báo chào mừng"

    def create_records_by_thread(self):
        print("Creating 10K records by thread")
        start_time = time.time()
        for i in range(10000):
            Student.objects.create(name=f"Student 1thread {i}", age=1)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")




    def create_records(self, start_index, end_index):
        for i in range(start_index, end_index):
            Student.objects.create(name=f"Student 10threads {i}", age=2)

    def create_records_by_10_threads(self):
        print("Creating 10K records by 10 threads")
        start_time = time.time()
        threads = []
        for i in range(10):
            t = threading.Thread(target=self.create_records, args=(i * 1000, (i + 1) * 1000))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")




    async def create_record(self, index):
        await Student.objects.acreate(name=f"Student async {index}", age=3)

    async def create_records_by_async(self):
        tasks = [self.create_record(i) for i in range(10000)]
        await asyncio.gather(*tasks)




    def handle(self, *args, **kwargs):
        self.create_records_by_thread()
        self.create_records_by_10_threads()
        print("Creating 10K records by async")
        start_time = time.time()
        asyncio.run(self.create_records_by_async())
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
