class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self) -> int:
        """
        Возвращает количество лошидиных сил для автомобиля
        """
        return 100


class Nissan(Car, Vehicle):
    vehicle_type = "crossover"
    price = 2000000

    def horse_powers(self) -> int:
        """
        Возвращает количество лошидиных сил для Nissan
        """
        return 200


# Создание экземпляра класса Nissan
nissan = Nissan()

# Вывод свойств экземпляра
print("Тип автомобиля:", nissan.vehicle_type)
print("Цена:", nissan.price)

# Результат выполнения кода
"""
Тип автомобиля: crossover
Цена: 2000000
"""
