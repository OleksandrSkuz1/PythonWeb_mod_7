from datetime import date, timedelta
import random
from faker import Faker

from models import Teacher, Student, Group, Subject, Grade
from connection import session

fake = Faker('uk-UA')

# Функція для створення випадкової дати
def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Додамо групи
groups = ['Group A', 'Group B', 'Group C']
for group_name in groups:
    group = Group(name=group_name)
    session.add(group)

# Додамо викладачів
teachers = []
for _ in range(5):
    teacher = Teacher(full_name=fake.name())
    session.add(teacher)
    teachers.append(teacher)

# Додамо предмети
subjects = []
for _ in range(8):
    teacher_id = random.choice(teachers).id
    subject = Subject(name=fake.catch_phrase(), teacher_id=teacher_id)
    session.add(subject)
    subjects.append(subject)


# Додамо студентів
for _ in range(30):
    student = Student(full_name=fake.name(), group_id=random.randint(1, 3))
    session.add(student)

# Додамо оцінки
for student in session.query(Student):
    for subject in subjects:
        grade = Grade(student_id=student.id, subject_id=subject.id, grade=random.randint(1, 10),
                      grade_date=random_date(date(2022, 1, 1), date.today()))
        session.add(grade)

# Зберігаємо зміни
session.commit()

# Закриваємо сесію
session.close()


