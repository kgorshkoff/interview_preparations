# 6. Проверить на практике возможности полиморфизма.
# Необходимо разделить дочерний класс ItemDiscountReport на два класса. Инициализировать классы необязательно.
# Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара,
# а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_price(self, price):
        self.__price = price


class ItemDiscountReportName(ItemDiscount):
    def get_info(self):
        return f'{self._ItemDiscount__name}'


class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        return f'{self._ItemDiscount__price}'


fc = ItemDiscountReportName('Трусы', 300)
sc = ItemDiscountReportPrice('Трусы', 300)

for i in (fc, sc):
    print(i.get_info())
