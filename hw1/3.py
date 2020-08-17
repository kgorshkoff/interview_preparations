"""
3. Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""

import random


def generate_random(start, stop):
    result_list = []
    result_dict = {}

    for i in range(10):
        new_random = int((stop - start) * random.random() + start)
        result_list.append(new_random)
        result_dict.update({f'elem_{new_random}': new_random})

    print(result_list, result_dict)


generate_random(23, 122)