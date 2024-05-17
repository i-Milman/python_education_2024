class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        return False


# Создаем два объекта Building
building1 = Building(5, "Жилое")
building2 = Building(5, "Жилое")
building3 = Building(3, "Магазин")

# Сравниваем объекты с использованием __eq__
print(building1 == building2)  # True
print(building1 == building3)  # False
