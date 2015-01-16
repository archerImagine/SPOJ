inputs = int(raw_input())

while inputs:
	myInput = raw_input()
	value1,value2 = myInput.split()

	for num in range(int(value1), int(value2) + 1):
		if num > 1:
			for i in range(2,num):
				if (num % i) == 0:
					break
			else:
				print num
	print ""
	inputs -= 1
