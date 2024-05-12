def data_sum (*args):
	result = 0
	for arg in args:
		if isinstance(arg, int): 
			result += arg #числа прибавляю
		elif isinstance(arg, str):
			result += len(arg) #символы считаю
		elif isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set): 
		    result += data_sum(*arg) #списки,кортежи и множества раскрываю
		elif isinstance(arg, dict):
			for key, value in arg.items(): #словари разбиваю на ключи и значения
				result += data_sum(key)
				result += data_sum(value)
	return result

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
] # входные данные

print(data_sum(data_structure)) #вывод результата