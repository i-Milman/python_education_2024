x = 38
print ('дратути!') # выполняется
if x < 0:
	print ('меньше нуля') # не выполняется
print ('дотвидания') # выполняется

a,b = 10, 5
if a > b:
	print ('a > b') # выполняется
if a > b and a > 0:
	print ('успех') # выполняется
if a > b and (a > 0 or b < 1000):
	print ('успех') # выполняется
if 5 < b and b < 10:
	print ('успех') # не выполняется

if '34' > '123':
	print ('успех') # выполняется
if '34' > '123':
	print ('успех') # выполняется
if [1,2] > [1,1]:
	print ('успех') # не выполняется

# Операция > между экземплярами типов str и int не поддерживается:
#if '6' > 5:
#	print ('успех')

# Операция > между экземплярами типов list и int не поддерживается:
#if [5,6] > 5:
#	print ('успех')

if '6' != 5:
	print ('успех') # выполняется
