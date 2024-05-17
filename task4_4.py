class Building:
    total = 0

    def __init__(self):
        Building.total += 1


# Создаю 40 объектов класса Building в цикле
buildings = []
for i in range(40):
    building = Building()
    buildings.append(building)
    print(building)

# Вывожу общее количество созданных объектов
print(f"Всего создано {Building.total} объектов класса Building")