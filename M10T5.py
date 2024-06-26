"""
Задание:
Моделирование программы для управления данными о движении товаров на складе
и эффективной обработки запросов на обновление информации в многопользовательской среде.

Представим, что у вас есть система управления складом,
где каждую минуту поступают запросы на обновление информации о поступлении товаров и отгрузке товаров.
Наша задача заключается в разработке программы,
которая будет эффективно обрабатывать эти запросы в многопользовательской среде,
с использованием механизма мультипроцессорности для обеспечения быстрой реакции на поступающие данные.

Создайте класс WarehouseManager - менеджера склада, который будет обладать следующими свойствами:
Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
Есть 2 действия: receipt - получение, shipment - отгрузка.
а) В случае получения данные должны поступить в data (добавить пару, если её не было и изменить значение ключа,
если позиция уже была в словаре)
б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).

3.Метод run - принимает запросы и создаёт для каждого свой параллельный процесс,
запускает его(start) и замораживает(join).
"""

# Решение:
from multiprocessing import Process, Queue


# from time import sleep


class WarehouseManager:
    """
    менеджера склада
    """

    def __init__(self):
        """
        Инициализация класса
        """
        self.data = dict()
        self.collector = Queue()

    def run(self, requests) -> None:
        """
        Метод распределяет запросы по процессам и собирает результаты
        :param requests: Список запросов
        """
        processes = [Process(target=self.process_request, args=request) for request in requests]
        [process.start() for process in processes]
        [process.join() for process in processes]
        while not self.collector.empty():
            data = self.collector.get()
            products = set(self.data).union(set(data))
            self.data = {product: self.data.get(product, 0) + data.get(product, 0) for product in products}

    def process_request(self, *request):
        """
        Метод реализует запрос (действие с товаром)
        :param request: кортеж с данными
        """
        product, action, quantity = request
        self.collector.put({product: (quantity if action == 'receipt'
                                      else -quantity if action == 'shipment'
                                      else 0)})


# Проверка:
if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)
