def convert(expr):
	output = []
	operator = []

	for char in expr:
		if char.isalpha():
			output.append(char)
		elif char in ['+','-','*','/',"^"]:
			operator.append(char)
		elif char == ')':
			output.append(operator.pop())
	return ''.join(output)

inputs = int(raw_input())
while inputs:
	expr = str(raw_input())
	print convert(expr)
	inputs -= 1


