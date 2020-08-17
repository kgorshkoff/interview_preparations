"""
1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции.
Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""


def multiplication_matrix(x, y):
    result = []
    tmp = []

    for vert_row in range(y + 1):
        result.append([vert_row])

        for hor_row in range(1, x + 1):
            if vert_row != 0:
                result[vert_row].append(vert_row * hor_row)
            else:
                result[vert_row].append(hor_row)


    converter = lambda j: [print('\t'.join(map(str, i))) for i in j]
    print(f'Таблица умножения {x} на {y}')
    converter(result)


multiplication_matrix(10, 10)
