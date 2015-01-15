# SPOJ: http://www.spoj.com/problems/ADDREV/
def reverseString(n):
	return n[::-1]

inputs = int(raw_input())

while inputs:
	myInput = raw_input()
	value1,value2 = myInput.split()
	print int(reverseString(str(int(reverseString(value1)) + int(reverseString(value2)))))
	inputs -= 1

