class Building:
    total = 0

    def __init__(self):
        Building.total += 1


# Создаем 40 объектов класса Building в цикле
buildings = []
for i in range(40):
    building = Building()
    buildings.append(building)

# Выводим созданные объекты на экран
for building in buildings:
    print(building)

# Выводим общее количество созданных объектов
print(f"Всего создано {Building.total} объектов класса Building")