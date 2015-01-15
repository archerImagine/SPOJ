# SPOJ: http://www.spoj.com/problems/FCTRL2/
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)


inputs = int(raw_input())
while inputs:
	value = int(raw_input())
	print factorial(value)
	inputs -= 1
			