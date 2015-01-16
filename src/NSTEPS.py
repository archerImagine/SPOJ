def nstep(x,y):
	if x != y and x-y != 2:
		print "No Number\n"
		return

	if x % 2 ==0 and y % 2 == 0:
		print x + y
	else:
		print x + y -1


inputs = int(raw_input())
while inputs:
	myInput = raw_input()
	value1,value2 = myInput.split()
	nstep(int(value1), int(value2))
	inputs -= 1
