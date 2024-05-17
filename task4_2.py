class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        """
        Метод изменяет атрибут numberOfFloors на параметр floors и выводит в консоль numberOfFloors
        """
        self.numberOfFloors = floors
        print(self.numberOfFloors)


house = House()
house.setNewNumberOfFloors(99)