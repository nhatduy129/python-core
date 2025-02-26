import pytest
from concurrent.futures import ThreadPoolExecutor, as_completed
from demoapp.models import NormalUser
import threading
from django.db import connection


@pytest.mark.django_db(transaction=True)
class TestNormalUser:
    def add_balance(self, user_id: int, amount: int):
        user = NormalUser.objects.get(id=user_id)
        user.add_balance(amount)
        connection.close()
    
    def reduce_balance(self, user_id: int, amount: int):
        user = NormalUser.objects.get(id=user_id)
        user.reduce_balance(amount)
        connection.close()
    
    def test_concurrency(self):
        user = NormalUser.objects.create(_balance=1000)
        threads = []
        for i in range(100):
            thread1 = threading.Thread(target=self.add_balance, args=(user.id, 200))
            thread2 = threading.Thread(target=self.reduce_balance, args=(user.id, 100))
            threads.append(thread1)
            threads.append(thread2)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        user.refresh_from_db()
        assert user.get_balance() == 11000
    
    def test_add_balance_concurrency(self):
        user = NormalUser.objects.create(_balance=1000)
        threads = []
        for i in range(100):
            thread1 = threading.Thread(target=self.add_balance, args=(user.id, 200))
            threads.append(thread1)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        user.refresh_from_db()
        assert user.get_balance() == 21000
        
    def test_reduce_balance_concurrency(self):
        user = NormalUser.objects.create(_balance=1000)
        threads = []
        for i in range(100):
            thread1 = threading.Thread(target=self.reduce_balance, args=(user.id, 2))
            threads.append(thread1)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        user.refresh_from_db()
        assert user.get_balance() == 800