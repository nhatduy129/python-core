import asyncio
from asyncdatabase.models import Student
from django.test import TestCase
import pytest
from unittest.mock import patch, AsyncMock
import threading
from django.db import connection


async def create_student_async() -> Student:
    result = await Student.objects.filter(name="Student sync").afirst()
    return result


@pytest.fixture
def student():
    return Student.objects.create(name="Student sync", age=1)


@pytest.mark.django_db(transaction=True)
class TestStudentAsync:
    def test_create_student_async(self, student):
        async_mock = AsyncMock()
        async_mock.afirst.return_value = student
        with patch("asyncdatabase.models.Student.objects.filter", return_value=async_mock):
            student = asyncio.run(create_student_async())
            assert student.name == "Student sync"
            assert student.age == 1
