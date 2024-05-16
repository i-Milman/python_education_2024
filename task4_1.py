class house: # Класс
    def __init__(self): # Конструктор класса
        self.floors = 10 # Атрибут класса

    def print_floors(self): # Метод класса
        for floor in range(1, self.floors + 1):
            print(f"Текущий этаж равен {floor}")

new_house = house() # Создаем экземпляр класса house

new_house.print_floors() # Вызываем метод print_floors