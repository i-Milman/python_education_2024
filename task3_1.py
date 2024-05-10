def print_params(a = 1, b = 'строка', c = True):
	print (a, b, c)
	
print_params()
print_params(7)
print_params(6, 'str')
print_params(5, 'string', False)

print_params(b = 25) 
print_params(c = [1,2,3])

values_list = [3, 'str', True]
values_dict = {'a':2, 'b':'string', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [8, 'str']
print_params(*values_list_2, 42)

