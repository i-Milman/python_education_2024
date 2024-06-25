"""
Представим, что вы разрабатываете приложение для автосервиса.
В вашем приложении есть классы, представляющие различные типы транспортных средств,
которые могут обслуживаться в автосервисе.

Создайте базовый класс TransportVehicle,
который содержит общие свойства и методы для всех типов транспортных средств, такие как:

- brand (марка)
- model (модель)
- year (год выпуска)
- registration_number (регистрационный номер)
- get_info() (метод, возвращающий информацию о транспортном средстве)

Затем создайте производные классы, унаследованные от TransportVehicle:

1. Car - представляет легковые автомобили. Дополнительно содержит:
   - engine_capacity (объем двигателя)
   - fuel_type (тип топлива)
   - num_of_doors (количество дверей)

2. Motorcycle - представляет мотоциклы. Дополнительно содержит:
   - engine_cc (объем двигателя в кубических сантиметрах)
   - is_scooter (флаг, указывающий, является ли мотоцикл скутером)

3. Truck - представляет грузовые автомобили. Дополнительно содержит:
   - payload_capacity (грузоподъемность)
   - num_of_axles (количество осей)

Реализуйте каждый класс со своими методами, например, get_engine_info(), get_vehicle_type() и т.д.

Затем в основной программе создайте несколько объектов каждого класса,
продемонстрировав использование наследования.
Например, можно создать экземпляры Car, Motorcycle и Truck, вызвать их методы и убедиться,
что производные классы наследуют свойства и методы от базового класса TransportVehicle.

Данная задача позволит вам применить принципы объектно-ориентированного программирования,
в частности, наследование классов, для моделирования реальной предметной области.
"""
# Решение:


class TransportVehicle:
    """
    Базовый класс транспорта
    """

    def __init__(self, brand: str, model: str, year: int, registration_number):
        """
        Инициализация класса
        :param brand: Брэнд
        :param model: Модель
        :param year: Год выпуска
        :param registration_number: Регистрационный номер
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.registration_number = registration_number

    def get_info(self) -> str:
        """
        Метод возвращает информацию о транспортном средстве
        :return: Строка с информацией
        """
        return (f'Брэнд: {self.brand}\n' +
                f'Модель: {self.model}\n' +
                f'Год выпуска: {self.year}\n' +
                f'Регистрационный номер: {self.registration_number}\n')


class Car(TransportVehicle):
    """
    Класс-наследник класса Транспорта
    """

    def __init__(self, brand: str, model: str, year: int, registration_number, engine_capacity: float, fuel_type: str,
                 num_of_doors: int):
        """
        Инициализация класса
        :param brand: Брэнд
        :param model: Модель
        :param year: Год выпуска
        :param registration_number: Регистрационный номер
        :param engine_capacity: объем двигателя
        :param fuel_type: тип топлива
        :param num_of_doors: количество дверей
        """
        super(Car, self).__init__(brand, model, year, registration_number)
        self.engine_capacity = engine_capacity
        self.fuel_type = fuel_type
        self.num_of_doors = num_of_doors

    def get_info(self) -> str:
        """
        Метод возвращает информацию о транспортном средстве
        :return: Строка с информацией
        """
        text = super().get_info()
        return text + (f'Объём двигателя: {self.engine_capacity}\n' +
                       f'Тип топлива: {self.fuel_type}\n' +
                       f'Количество дверей: {self.num_of_doors}\n')


class Motorcycle(TransportVehicle):
    """
    Класс-наследник класса Транспорта
    """

    def __init__(self, brand: str, model: str, year: int, registration_number: str,
                 engine_cc: int, is_scooter: bool):
        """
        Инициализация класса
        :param brand: Брэнд
        :param model: Модель
        :param year: Год выпуска
        :param registration_number: Регистрационный номер
        :param engine_cc: объем двигателя в кубических сантиметрах
        :param is_scooter: флаг, указывающий, является ли мотоцикл скутером
        """
        super(Motorcycle, self).__init__(brand, model, year, registration_number)
        self.engine_cc = engine_cc
        self.is_scooter = is_scooter

    def get_info(self) -> str:
        """
        Метод возвращает информацию о транспортном средстве
        :return: Строка с информацией
        """
        text = super().get_info()
        return text + (f'Объём двигателя (см3): {self.engine_cc}\n' +
                       f'Скутер: {'Да' if self.is_scooter else 'Нет'}\n')

    def get_engine_info(self):
        return f'Объём двигателя (см3): {self.engine_cc}'

    def get_vehicle_type(self):
        return f'Скутер: {'Да' if self.is_scooter else 'Нет'}'


class Truck(TransportVehicle):
    """
        Класс-наследник класса Транспорта
        """

    def __init__(self, brand: str, model: str, year: int, registration_number: str, payload_capacity: float,
                 num_of_axles: int):
        """
        Инициализация класса
        :param brand: Брэнд
        :param model: Модель
        :param year: Год выпуска
        :param registration_number: Регистрационный номер
        :param payload_capacity: грузоподъемность
        :param num_of_axles: количество осей
        """
        super(Truck, self).__init__(brand, model, year, registration_number)
        self.payload_capacity = payload_capacity
        self.num_of_axles = num_of_axles

    def get_info(self) -> str:
        """
        Метод возвращает информацию о транспортном средстве
        :return: Строка с информацией
        """
        text = super().get_info()
        return text + (f'Грузоподъемность: {self.payload_capacity}\n' +
                       f'Количество осей: {self.num_of_axles}\n')


# Проверка:

# Создаем объекты разных транспортных средств
car = Car(brand='Toyota', model='Corolla', year=2018, registration_number='ABC123',
          engine_capacity=1.8, fuel_type='Gasoline', num_of_doors=4)

motorcycle = Motorcycle(brand='Honda', model='CBR600RR', year=2015, registration_number='XYZ456',
                        engine_cc=599, is_scooter=False)

truck = Truck(brand='Volvo', model='FH16', year=2020, registration_number='DEF789',
              payload_capacity=20000, num_of_axles=4)

# Вывод информации об объектах
print(car.get_info())
print(motorcycle.get_info())
print(truck.get_info())

# Вызов дополнительных методов
print(motorcycle.get_engine_info())
print(motorcycle.get_vehicle_type())
