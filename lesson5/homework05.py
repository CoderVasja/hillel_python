# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1 - Додаєм нову запис на початок листа
my_info = ('Vasilii', 'Makogon', 26, 'QA Engineer', 'Mykolaiv')
people_records.insert(0, my_info)

# 2 - Свапаємо єлементи 1 та 5 місцями

# Варіант 1 (Перший який прийшов в голову)

# Спочатку вивів поточні єлементи
print(people_records[1])
print(people_records[5])
people_records.insert(1, people_records[5])  # Вставляєм єлемент з індексом 5 на перший індекс
people_records.insert(5, people_records[2])  # Так як ми знаємо що запис який був під індексом 1 тепер під індексом 2 то вставляєм запис 2 під індекс 5
print('-' * 100)

# Вивів вже свапнуті щоб пересвідчитись чи точно вони сванулись
print(people_records[1])
print(people_records[5])
print('-' * 100)

# #Варіант 2
# i, j = 1, 5
# people_records[i], people_records[j] = people_records[j], people_records[i]
# print(people_records[1])
# print(people_records[5])

# 3 Визначаємо рік
ages = [people_records[i][2] for i in [6, 10, 13]]
result = all(x>=30 for x in ages)
print(result)



