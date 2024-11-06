#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
decor_el = "-"*32
print(alice_in_wonderland)
print(decor_el)
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""


black_sea = 436402
azov_sea = 37800
total = black_sea + azov_sea
print(f"Загальня площа Чорного та Азовского моря: {total} км2" )
print(decor_el)
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375291 #всього товарів
storages12 = 250449 #товарів на складі 1 та 2
storages23 = 222950 #товарів на складі 2 та 3

goods_on_3 = total_goods - storages12 # дізнаємось скільки товарів на складі 3
goods_on_2 = storages23 - goods_on_3 # дізнаємось скільки товарів на складі 2
goods_on_1 = storages12 - goods_on_2 # дізнаємось скільки товарів на складі 1

info_text = (
f'На 1 складі знаходится: {goods_on_1} товарів\n'
f'На 2 складі знаходится: {goods_on_2} товарів\n'
f'На 3 складі знаходится: {goods_on_3} товарів'
)

print(info_text)
print(decor_el)


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
total_months = 18
price_per_moth = 1179
total_price = 18*1179
print(f"Загальна вартість компьютера буде {total_price}")
print(decor_el)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(
    f'Остача від діленя\n'
    f'a) {a}\n'
    f'b) {b}\n'
    f'c) {c}\n'
    f'd) {d}\n'
    f'e) {e}\n'
    f'f) {f}'
    )
print(decor_el)
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_total = 4*274
medium_pizza_total = 2*218
juce = 4*35
cake = 350
water = 3*21
total_check = big_pizza_total + medium_pizza_total + juce + cake + water
print(f'Загальня сумма замовленя: {total_check} грн')
print(decor_el)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photo_per_page = 8
total_pages = total_photos/photo_per_page
print(f'Щоб вклеїти усі фото Ігорю знадобится {int(total_pages)} сторінок')
print(decor_el)
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance = 1600
tank_capacity = 48
gass_per_km = 9
total_gass = total_distance/100*gass_per_km
number_refills = int(total_gass/tank_capacity)
print(f'Для такої поїздки знадобится {total_gass} літрів бензину'
      f' та родина зупинится {number_refills} рази для дозаправки')
print(decor_el)