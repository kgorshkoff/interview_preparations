"""
5. Усовершенствовать первую функцию из предыдущего примера.

Необходимо просканировать текстовый файл, созданный на предыдущем задании
и реализовать создание и запись нового текстового файла

В новый текстовый файл обеспечить запись строк вида:

zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...

Т.е. извлекаются строки из первого текстового файла
а в новый они записываются в виде, где вместо числа ставится строка

Здесь необходимо использовать регулярные выражения.
"""


import os
import re
import random
import string


def generator(file_name):
    try:
        file = open(file_name, 'w')
    except FileExistsError as e:
        return print(f'File "{e.filename}" already exists')

    nums, strings = [], []

    for _ in range(10):
        nums.append(random.randint(1, 100))
        strings.append(''.join(random.choice(string.ascii_letters) for _ in range(10)))

    for i in list(zip(nums, strings)):
        file.write(f'{i[0]} {i[1]}\n')

    file.close()
    reader(os.open(file_name, os.O_RDONLY))


def reader(file_descriptor):
    file = os.fdopen(file_descriptor, 'r')
    with open('new_test.txt', 'w') as nf:
        for line in file:
            nf.write(re.sub(r'(\d+) (\w*)', r'\2 \2', line))
    file.close()


generator('test.txt')
