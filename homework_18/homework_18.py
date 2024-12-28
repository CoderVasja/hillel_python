"""
ГЕНЕРАТОРИ
"""

#1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers_generator(N):
    for num in range(0, N + 1, 2):
        yield num


N = 20
even_numbers = even_numbers_generator(N)
for number in even_numbers:
    print(number)

print('--'*80)

#2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

N = 50
for number in fibonacci_generator(N):
    print(number)


"""ІТЕРАТОРИ"""
print('--'*80)
#1. Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseNumbersIter:

    def __init__(self, lst):
        self.lst = lst
        self.current_pos = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_pos < 0:
            raise StopIteration
        result =  self.lst[self.current_pos]
        self.current_pos -= 1
        return result

numbers = ReverseNumbersIter([1, 2, 3, 4, 5])
for num in numbers:
    print(num)


print('--'*80)
#2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class EvenNumbersIter:

    def __init__(self, max_num):
        self.max_num = max_num
        self.current_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_pos > self.max_num:
            raise StopIteration

        if self.current_pos <= self.max_num:
            result = self.current_pos
            self.current_pos += 2

            return result

numbers = EvenNumbersIter(5)
print(next(numbers))
print(next(numbers))
print(next(numbers))


"""
ДЕКОРАТОРИ
"""
#1. Напишіть декоратор, який логує аргументи та результати викликаної функції.

print('--'*80)
def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_arguments_and_result
def add(a, b):
    return a + b

add(2, 3)

@log_arguments_and_result
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Vasya", greeting="Hi")

#2. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
print('--'*80)
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))