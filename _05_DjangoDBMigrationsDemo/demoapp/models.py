from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    state = models.CharField(max_length=100)
    country = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.name
