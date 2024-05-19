class Car:
    price = 1000000

    def horse_powers(self) -> int :
        return 1 # Лошадиные силы по умолчанию


class Nissan(Car):
    price = 2000000

    def horse_powers(self) -> int :
        return 200 # Лошадиные силы Nissan


class Kia(Car):
    price = 1500000

    def horse_powers(self) -> int :
        return 150 # Лошадиные силы Kia


# Примеры использования
nissan = Nissan()
print("Nissan - цена:", nissan.price)
print("Nissan - лошадиные силы:", nissan.horse_powers())

kia = Kia()
print("Kia - цена:", kia.price)
print("Kia - лошадиные силы:", kia.horse_powers())

# Результат выполнения кода
"""
Nissan - цена: 2000000
Nissan - лошадиные силы: 200
Kia - цена: 1500000
Kia - лошадиные силы: 150
"""