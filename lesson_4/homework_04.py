adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
import re
dec_el = '-'*100
##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.d
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)
print(dec_el)
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
print(dec_el)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)
print(dec_el)
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count('h')
print(f'Буква h зустрічається у тексті {count_h} разів')
print(dec_el)
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
capitalized_words = re.findall(r'\b[A-Z]', adwentures_of_tom_sawer)
count = len(capitalized_words)
print(f'Кількість слів, що починаються з великої літери: {count}')
print(dec_el)
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_position = adwentures_of_tom_sawer.find("Tom") #Знаходим переше входженя
second_position = adwentures_of_tom_sawer.find("Tom", first_position + 1) #Знаходим друге входженя після першого
print(f'Позиция второго вхождения слова "Tom": {second_position}')
print(dec_el)
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
print(adwentures_of_tom_sawer_sentences)
print(dec_el)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(adwentures_of_tom_sawer_sentences[3].lower())
print(dec_el)
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
found = re.search(r'(^|[.!?]\s)By the time', adwentures_of_tom_sawer)
if found:
    print('У тексті є речення яке починаєтся з By the time')
else:
    print('У тексті немає речення яке починаєтся з By the time')
print(dec_el)
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
print(f'Останє речення текст: {last_sentence}')
print(f'В останьому речені тексту {len(last_sentence.split())} слова')
