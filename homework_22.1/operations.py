from students import session, Student, Course


def add_student(name: str, email: str, course_names: list):
    student = Student(name=name, email=email)
    session.add(student)

    for course_name in course_names:
        course = session.query(Course).filter_by(name=course_name).first()
        if course:
            student.courses.append(course)

    session.commit()


def get_courses_for_student(student_name: str) -> list:
    student = session.query(Student).filter_by(name=student_name).first()
    return student.courses if student else []


def get_students_in_course(course_name: str) -> list:
    course = session.query(Course).filter_by(name=course_name).first()
    return course.students if course else []


def update_student_email(student_name: str, new_email: str):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        student.email = new_email
        session.commit()


def delete_student(student_name: str):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        session.delete(student)
        session.commit()

def get_student_by_name(student_name: str) -> Student:
    student = session.query(Student).filter_by(name=student_name).first()
    return student




# Додати нового студента
add_student("John Doe", "john@doe.com", ["Mathematics", "Programming"])
student = get_student_by_name("John Doe")

if student:
    print(f"ID: {student.id}, Name: {student.name}, Email: {student.email}")
else:
    print("Студент не знайдений.")

# Отримати курси студента
john_courses = get_courses_for_student("John Doe")
print([c.name for c in john_courses])  # ['Mathematics', 'Programming']

# Отримати студентів на курсі
math_students = get_students_in_course("Mathematics")
print([s.name for s in math_students])

# Оновити email
update_student_email("John Doe", "new.john@doe.com")


if student:
    print(f"ID: {student.id}, Name: {student.name}, Email: {student.email}")
else:
    print("Студент не знайдений.")

# Видалити студента
delete_student("Student 1")
