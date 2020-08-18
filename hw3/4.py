"""
4. Написать программу, в которой реализовать две функции.

В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.

Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Например:
[91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
и
['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']


Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Например:
91 zmsebjvdgi

42 ychpwljtzn

...

Первая функция должна возвращать ссылку на файловый дескриптор


После вызова первой функции возвращаемый файловый дескриптор нужно передавать во вторую функцию
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
"""
import os
import random
import string


def generator(file_name):
    try:
        file = open(file_name, 'x')
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
    for line in file:
        print(line)
    file.close()


generator('test.txt')
