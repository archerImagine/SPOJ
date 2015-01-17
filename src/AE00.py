def fibonacci(x):
	"""assumes x an int >= 0
        Returns Fibonacci of x"""
	assert type(x) == int and x >=  0
	if x == 0:
		return 0
	elif x == 1:
		return 2
	else:
		return fibonacci(x-1) + fibonacci(x-2)

testCases = int(raw_input())

print fibonacci(testCases)
# print fibonacci(1)
# print fibonacci(2)
# print fibonacci(3)