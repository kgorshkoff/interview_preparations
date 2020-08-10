"""
2. Дополнить следующую функцию недостающим кодом:

def print_directory_contents(sPath):
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.
"""
import os


def print_directory_contents(path):
    arr = os.listdir(path)

    print(path, arr)

    for item in arr:
        current_path = os.path.join(path, item)

        if os.path.isdir(current_path):
            print_directory_contents(current_path)


print_directory_contents('/Users/kirill/Downloads')
