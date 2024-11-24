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


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


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

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_string(*args):
    reversed_string = ''.join(sorted(args, reverse=True))

    return reversed_string

# Variant 2

def reverse_string_2(string: str):
    reversed_string = string[::-1]

    return reversed_string


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(*args):
    message = ''
    longest = max(args, key=len)
    message = f'The longest word in the list: {longest}'

    return message

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    index = str1.find(str2)

    if str2 in str1:

        return index

    else:

        return -1


str1 = "Hello, world!"
str2 = "world"
 # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
  # поверне -1

# task 7
# task 8
# task 9
# task 10

"""
 Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 03 from homework 4
# Зробіть так, щоб у тексті було не більше одного пробілу між словами.


def remove_spaces(original_text: str):
    original_text = original_text.split()  # ділим орігінальний текст на слова

    text_without_space = ' '.join(original_text)  # з'єднуємо поділений текст розділивши його одним пробілом


adwentures_of_tom_sawer = """\
the retired artist sat on a barrel in the   shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no      lack of material;
boys happened along every little while;
they came to jeer, but       remained to whitewash. 
By the time Ben was      fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a     dead rat     and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken     boy in the     morning, Tom was literally
rolling in wealth."""

remove_spaces(adwentures_of_tom_sawer)


# task 01 from homework 6
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

def find_qnique_elements():
    string = input('Enter your string:')  # отримуємо строку
    unique_elements = set(string)  # через set філтруємо елементи які повторюються
    print(unique_elements)
    print(len(unique_elements) > 10)  # порівнюємо чи кількість унікальних елементів більше чим 10 чи ні



# task 03 from homework 6
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.

def find_string(*args):
    lst2 = []  # ініціалізація нового списку
    for s in args:
        if type(s) == str:  # якщо елемпнт списку це строка то додаємо його в новий список
            lst2.append(s)
    print(lst2)


# task 04 from homework 6 Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

def sum_of_even_numbers(*args):
    total = 0
    for number in args:
        if number % 2 == 0:  # перевіряємо якщо елемент списку ділится на два то це парне число
            total += number  # додаємо це число до загальної суми
    print(total)


