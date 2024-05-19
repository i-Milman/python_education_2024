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
print("Nissan Price:", nissan.price)
print("Nissan Horse Power:", nissan.horse_powers())

kia = Kia()
print("Kia Price:", kia.price)
print("Kia Horse Power:", kia.horse_powers())