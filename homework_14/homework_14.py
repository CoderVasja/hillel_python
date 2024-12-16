class Student:

    def __init__(self, name, surname, age, average_mark):

        self.name = name
        self.surname = surname
        self.average_mark = average_mark
        self.age = age

    def change_average_mark(self, new_average_mark):

        if not isinstance(new_average_mark, (int, float)):
            raise ValueError('Mark should be a number')
        if not 0 < new_average_mark <= 5:
            raise ValueError('Mark should be between 0 and 5')

        self.average_mark = new_average_mark


new_student = Student('Vasilii', 'Makogon', 22, 4.0)

print(f'Student name: {new_student.name} {new_student.surname}\nAge: {new_student.age}\nMark: {new_student.average_mark}')

new_student.change_average_mark(5)

print(f'\nStudent name: {new_student.name} {new_student.surname}\nAge: {new_student.age}\nNew Mark: {new_student.average_mark}')
