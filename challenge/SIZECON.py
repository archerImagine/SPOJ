inputs = int(raw_input())
count = 0
while inputs != 0:
	value = int(raw_input())
	
	if value > 0:
		count += value
	inputs -= 1

print count	

