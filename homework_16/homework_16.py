from abc import abstractmethod

import pytest

#Task 1

class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary, department):

        Employee.__init__(self, name,salary)
        self.department = department



class Developer(Employee):

    def __init__(self, name, salary, programming_language):

        Employee.__init__(self, name,salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):

    def __init__(self, name, salary, department, programming_language, team_size):

        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


#print(TeamLead.mro())


def test_check_attrs():

    my_team_lead = TeamLead('Denis', 4000, 'QA','Python',4)

    assert hasattr(my_team_lead, "name")
    assert hasattr(my_team_lead, "salary")
    assert hasattr(my_team_lead, "department")
    assert hasattr(my_team_lead, "programming_language")
    assert hasattr(my_team_lead, "team_size")



#Task 2

class Figure():

    @abstractmethod
    def area_calculate(self):
        pass

class Circle(Figure):

    def __init__(self, radius):

        if radius < 1:
            raise ValueError('Radius should be greater than 0')
        self.__radius = radius


    def area_calculate(self):
        return 3.14 * self.__radius ** 2


class Square(Figure):

    def __init__(self, side_a):
        if side_a < 1:
            raise ValueError('Side A should be greater than 0')
        self.__side_a = side_a

    def area_calculate(self):
        return self.__side_a ** 2


class Rectangle(Figure):

    def __init__(self, side_width, side_height):
        if side_width < 1:
            raise ValueError('Side width should be greater than 0')
        elif side_height < 1:
            raise ValueError('Side height should be greater than 0')
        self.__side_width = side_width
        self.__side_height = side_height

    def area_calculate(self):
        return self.__side_width * self.__side_height

my_rectangle = Rectangle(2,3)
my_circle = Circle(2)
my_square = Square(5)

shapes = [my_square, my_circle, my_rectangle]

for shape in shapes:
    print(f'Area for a {shape.__class__.__name__}: {shape.area_calculate()}')