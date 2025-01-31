from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

Base = declarative_base()

# Асоціативна таблиця для зв'язку many-to-many
enrollments = Table(
    'enrollments',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id', ondelete='CASCADE'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id', ondelete='CASCADE'), primary_key=True)
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    courses = relationship('Course', secondary=enrollments, back_populates='students')


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    students = relationship('Student', secondary=enrollments, back_populates='courses')


# Ініціалізація бази даних
engine = create_engine('sqlite:///university.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# Заповнення тестовими даними
def populate_sample_data():
    courses = [
        Course(name="Mathematics", description="Algebra and Calculus"),
        Course(name="Physics", description="Fundamentals of Physics"),
        Course(name="Chemistry", description="Basic Chemistry"),
        Course(name="Biology", description="Introduction to Biology"),
        Course(name="Programming", description="Python Programming")
    ]

    students = [Student(name=f"Student {i}", email=f"student{i}@edu.com") for i in range(1, 21)]

    for student in students:
        student.courses.extend(random.sample(courses, k=random.randint(1, 3)))

    session.add_all(courses + students)
    session.commit()


if __name__ == '__main__':
    populate_sample_data()