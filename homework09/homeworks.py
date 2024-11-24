# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    multiplier = 1
    results = []
    while multiplier <= 10:
        result = number * multiplier
        if result > 25:
            break
        results.append((number, multiplier, result))
        multiplier += 1
    return results


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_numbers(num1: int | float, num2: int | float):
    sum = num1 + num2
    return sum


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(*args):
    total = sum(args)
    numbers_quantity = len(args)

    arithmetic = total / numbers_quantity  # можна огорнути в int() якщо потрібне ціле значення

    return arithmetic

