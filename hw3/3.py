# 3. Создать два списка с различным количеством элементов.
# В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь.
# Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
# Значения, которым не хватило ключей, необходимо отбросить.

k = ['apple', 'pear', 'grape', 'banana', 'pineapple']
v = [12, 33, 95, 11, 2, 3, 66, 77]


def zipper(keys, values):
    result = {}

    for key in keys:
        result[key] = values[keys.index(key)] if keys.index(key) < len(values) else None

    print(result)


zipper(k, v)
zipper(k, v[:-5])
