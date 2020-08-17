# 5. Реализовать расчет цены товара со скидкой.
# Величина скидки должна передаваться в качестве аргумента в дочерний класс.
# Выполнить перегрузку методов конструктора дочернего класса
# (метод init, в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса.
# В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
# Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
# (вторая и третья строка после объявления дочернего класса).


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, __name, __price, discount):
        super().__init__(__name, __price)
        self.discount = discount

    def get_parent_data(self):
        print(self._ItemDiscount__name, self._ItemDiscount__price)

    def __str__(self):
        return f'{self._ItemDiscount__price - self._ItemDiscount__price / self.discount}'


item = ItemDiscountReport('Трусы', 300, 10)
item.get_parent_data()
print(item)
