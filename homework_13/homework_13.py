import csv
import json
from http.client import error
from pathlib import Path
import xml.etree.ElementTree as ET
import logging

"""
Завдання 1:

Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх. 
Результат запишіть у файл result_<your_second_name>.csv
"""
def remove_duplicate(file_1:str,file_2:str):

    #читаємо файли та записуємо їх у зміні
    with open(file_1) as csvfile_1,open(file_2) as csvfile_2:

        data_file_1 = csv.reader(csvfile_1)
        data_file_2 = csv.reader(csvfile_2)


        #Пропускаємо заголовки
        headers_data_file_1 = next(data_file_1)
        headers_data_file_2 = next(data_file_2)

        unique_rows = set(tuple(row) for row in data_file_1).union(tuple(row) for row in data_file_2)

    with open('unique_output.csv', 'w', newline='') as output:
        writer = csv.writer(output)

        # Записуємо заголовки
        writer.writerow(headers_data_file_1)

        # Записуємо заголовки унікальні записи
        writer.writerows(unique_rows)

remove_duplicate('random.csv','random-michaels.csv')



logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

"""
Завдання 2:

Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
Результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""
error_handler = logging.FileHandler('json_error.log',encoding='utf-8', mode='w')
error_handler.setLevel(logging.ERROR)
info_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_handler.setFormatter(info_formatter)
logger.addHandler(error_handler)

def found_invalid_json(path):
    base_path = Path(path)
    full_path = Path(__file__).parent / base_path
    files = [f for f in full_path.iterdir() if f.is_file()]

    for file_name in files:
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                print(f"Файл {file_name.name} прочитано.")
        except Exception as e:
            logger.error(f"Невідома помилка у файлі {file_name.name}")


found_invalid_json('work_with_json')



"""
Завдання 3:

Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number 
і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

error_handler = logging.FileHandler('xml_info.log', mode='w')
error_handler.setLevel(logging.INFO)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)
logger.addHandler(error_handler)


def find_incoming(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    for group in root.findall('group'):
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                message = f"Group: {group.find('name').text}, incoming: {incoming.text}"
            else:
                message = f"Group: {group.find('name').text}, incoming: Не знайдено"

        logger.info(message)

find_incoming('groups.xml')