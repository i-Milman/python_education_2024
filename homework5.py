my_list = ['apple', 'coconut', 'banana', 'orange', 'kiwi']
print ('Список: ', my_list)
print ('Первый элемент: ', my_list[0])
print ('Последний элемент: ', my_list[-1])
print ('Элементы 3-5: ', my_list[2:5])
my_list[2] = 'fish'
print ('Измененный список: ', my_list)

my_dict = { 'Matrix' : 1999, 'Equilibrium': 2002, 'Inception': 2010, 'In Time': 2011}
print ('Словарь: ', my_dict)
print ('Год выпуска "Matrix": ', my_dict.get('Matrix'))
my_dict['Matrix'] = 2000
print ('Измененный словарь: ', my_dict)