def test (*args):
	for arg in args:
		print(arg)
		
def factorial (n):
	if n == 0:
		return 1 # 0! = 1
	else:
		return n * factorial(n - 1) # n! = n * (n - 1)!
		
#test(465,345,665,987) #любые переменные любого количества
#print(factorial(5)) #только одна int >= 0
