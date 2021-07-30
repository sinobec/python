func1 = lambda arug: arug * 3
print(func1(5))

def func(arug):
	return lambda x: x * arug
caul = func(2) #此时调用了func的arug
result = caul(12) #此时调用了lambda的x = 12
print(result)
