class house:
    def __init__(self):
        self.floors = 10

    def print_floors(self):
        for floor in range(1, self.floors + 1):
            print(f"Текущий этаж равен {floor}")

new_house = house() # Создаем экземпляр класса House

new_house.print_floors() # Вызываем метод printFloors