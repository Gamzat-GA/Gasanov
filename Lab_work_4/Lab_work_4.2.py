
import json
import os


def calculate_product_sum(json_file_path):
    # Открываем файл и загружаем данные из JSON
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Инициализиция переменной для суммы произведений
    sum_of_products = 0

    for item in data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)
        sum_of_products += score * weight
    sum_of_products_rounded = round(sum_of_products, 3)
    return sum_of_products_rounded


def task() -> float:
    # Получение текущей директории скрипта
    script_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_directory, "input.json")
    result = calculate_product_sum(json_file_path)
    return result


print(task())
