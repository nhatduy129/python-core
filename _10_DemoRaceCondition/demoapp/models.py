import pytest
from django.db import models, transaction, connection
from django.db.models import F


class BadUser(models.Model):
    id = models.AutoField(primary_key=True)
    _balance = models.IntegerField(default=0)
    
    def get_balance(self):
        return self._balance
    
    def add_balance(self, amount: int):
        self._balance += amount
        self.save(update_fields=["_balance"])
        
    def reduce_balance(self, amount: int):
        self._balance -= amount
        self.save()


class NormalUser(models.Model):
    id = models.AutoField(primary_key=True)
    _balance = models.IntegerField(default=0)
    
    def get_balance(self):
        return self._balance
    
    @transaction.atomic
    def add_balance(self, amount: int):
        user = NormalUser.objects.select_for_update().get(id=self.id)
        user._balance += amount
        user.save(update_fields=["_balance"])
        
    @transaction.atomic
    def reduce_balance(self, amount: int):
        user = NormalUser.objects.select_for_update().get(id=self.id)
        if user._balance >= amount:
            user._balance -= amount
            user.save(update_fields=["_balance"])
        else:
            raise ValueError("Not enough balance")
        

class GoodUser(models.Model):
    id = models.AutoField(primary_key=True)
    _balance = models.IntegerField(default=0)
    
    def get_balance(self):
        return self._balance

    def add_balance(self, amount: int):
        GoodUser.objects.filter(id=self.id).update(_balance=F("_balance") + amount)
        
    def reduce_balance(self, amount: int):
        updated_rows = GoodUser.objects.filter(id=self.id, _balance__gte=amount).update(
            _balance=F("_balance") - amount
        )
        if updated_rows == 0:
            raise ValueError("Not enough balance")