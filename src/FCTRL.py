# SPOJ : http://www.spoj.com/problems/FCTRL/
inputs = int(raw_input())
count = 0
while inputs:
	value = int(raw_input())
	count = 0
	while (value >= 5):
		count += value/5
		value /= 5
		# print value, count
	inputs -= 1
	print count