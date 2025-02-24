from django.test import TestCase
from demoapp.models import Author, Book, Student, Course, Company, Employee, Project, Coder
import pytest


class TestModels(TestCase):
    def test_many_to_many_models_case_1(self):
        author1 = Author.objects.create(name='John Doe', email='john.doe@example.com')
        author2 = Author.objects.create(name='Jane Doe', email='jane.doe@example.com')
        book1 = Book.objects.create(title='Book 1')
        book2 = Book.objects.create(title='Book 2')
        pytest.set_trace()
        book1.authors.add(author1)
        book1.authors.add(author2)
        author1.book_authors.add(book1)
        author1.book_authors.add(book2)
        self.assertEqual(book1.authors.all().count(), 2)
        self.assertEqual(book2.authors.all().count(), 1)
        self.assertEqual(author1.book_authors.all().count(), 2)
        
    def test_many_to_many_models_case_2(self):
        student1 = Student.objects.create(name='John Doe', email='john.doe@example.com')
        student2 = Student.objects.create(name='Jane Doe', email='jane.doe@example.com')
        course1 = Course.objects.create(title='Course 1')
        course2 = Course.objects.create(title='Course 2')
        course1.students.add(student1)
        course1.students.add(student2)
        student1.courses.add(course1)
        student1.courses.add(course2)
        self.assertEqual(course1.students.all().count(), 2)
        self.assertEqual(course2.students.all().count(), 1)
        self.assertEqual(student1.courses.all().count(), 2)

    def test_one_to_many_models_case_1(self):
        company = Company.objects.create(name='Company 1')
        employee1 = Employee.objects.create(name='John Doe', company=company)
        employee2 = Employee.objects.create(name='Jane Doe', company=company)
        self.assertEqual(company.employees.all().count(), 2)
        self.assertEqual(employee1.company, company)
        self.assertEqual(employee2.company, company)

    def test_one_to_many_models_case_2(self):
        project = Project.objects.create(name='Project 1')
        coder1 = Coder.objects.create(name='John Doe', project=project)
        coder2 = Coder.objects.create(name='Jane Doe', project=project)
        self.assertEqual(project.project_coders.all().count(), 2)
        self.assertEqual(coder1.project, project)
        self.assertEqual(coder2.project, project)