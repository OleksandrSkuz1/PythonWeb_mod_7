"""-- Створення таблиці груп
DROP TABLE IF EXISTS Groups;
CREATE TABLE Groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);


-- Створення таблиці студентів
DROP TABLE IF EXISTS Students;
CREATE TABLE Students (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    group_id INTEGER REFERENCES Groups(id)
    on delete cascade

);


-- Створення таблиці викладачів
DROP TABLE IF EXISTS Teachers;
CREATE TABLE Teachers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL

);

-- Створення таблиці предметів
DROP TABLE IF EXISTS Subjects;
CREATE TABLE Subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(175) NOT NULL,
    teacher_id INTEGER REFERENCES Teachers(id)
      on delete cascade
);

-- Створення таблиці оцінок
DROP TABLE IF EXISTS Grades;
CREATE TABLE Grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES Students(id) ON DELETE CASCADE,
    subject_id INTEGER REFERENCES Subjects(id) ON DELETE CASCADE,
    grade INTEGER CHECK (grade >= 0 and grade <= 100),
    grade_date DATE NOT NULL
);"""

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

class Groups(Base):
    __tablename__ = 'Groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Students(Base):
    __tablename__ = 'Students'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    group_id = Column(Integer, ForeignKey('Groups.id'), nullable=False)


class Teachers(Base):
    __tablename__ = 'Teachers'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)


class Subjects(Base):
    __tablename__ = 'Subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(175), nullable=False)
    teacher_id = Column(Integer, ForeignKey('Teachers.id'), nullable=False)


class Grades(Base):
    __tablename__ = 'Grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('Students.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('Subjects.id'), nullable=False)
    grade = Column(Integer, nullable=False)
    grade_date = Column(Date, nullable=False)


