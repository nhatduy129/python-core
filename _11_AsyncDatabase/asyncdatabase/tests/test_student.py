import asyncio
from asyncdatabase.models import Student
import pytest


async def filter_then_get_first_student_async() -> Student:
    result = await Student.objects.filter(name="Student A").afirst()
    return result


async def create_student_async() -> Student:
    result = await Student.objects.acreate(name="Student B", age=2)
    return result


async def get_all_students_async() -> list[Student]:
    result = [student async for student in Student.objects.all()]
    print(result)
    return result


async def filter_students_async():
    result = Student.objects.filter(age=1)
    async for student in result:
        print("ok")
    return result

async def count_students_async():
    result = await Student.objects.acount()
    return result

async def filter_then_all_students_async():
    result = [student async for student in Student.objects.filter(age=1).all()]
    print(result)
    return result


@pytest.fixture
def student():
    return Student.objects.create(name="Student A", age=1)

@pytest.fixture
def student2():
    return Student.objects.create(name="Student B", age=2)


@pytest.mark.django_db
class TestStudentAsync:
    @pytest.mark.asyncio
    def test_filter_then_get_first_student_async(self, student):
        student = asyncio.run(filter_then_get_first_student_async())
        assert student.name == "Student A"
        assert student.age == 1

    @pytest.mark.asyncio
    def test_create_student_async(self, student):
        student = asyncio.run(create_student_async())
        assert student.name == "Student B"
        assert student.age == 2
        assert Student.objects.count() == 2

    @pytest.mark.asyncio
    def test_get_all_students_async(self, student, student2):
        students = asyncio.run(get_all_students_async())
        assert len(students) == 2
        assert students[0].name == "Student A"
        assert students[0].age == 1
        assert students[1].name == "Student B"
        assert students[1].age == 2

    @pytest.mark.asyncio
    def test_filter_students_async(self, student):
        asyncio.run(filter_students_async())

    @pytest.mark.asyncio
    def test_count_students_async(self, student):
        asyncio.run(count_students_async())

    @pytest.mark.asyncio
    def test_filter_then_all_students_async(self, student, student2):
        asyncio.run(filter_then_all_students_async())
