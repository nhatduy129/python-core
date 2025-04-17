from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='book_authors')


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Coder(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_coders')

    def __str__(self):
        return self.name


class Chatbot(models.Model):
    name = models.CharField(max_length=100)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='chatbot')
    demo_service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='demo_chatbot')
    auto_reply = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
