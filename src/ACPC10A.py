inputs = raw_input()

value1,value2,value3 = inputs.split()

value1 = int(value1)
value2 = int(value2)
value3 = int(value3)

def isAP(value1,value2,value3):
	if (value2 - value1) == (value3 - value2):
		return "AP"

def isGP(value1,value2,value3):
	if (value2/value1) == (value3/value2):
		return "GP"

while value1 != 0 and value2 != 0 and value3 != 0:
	if isAP(value1,value2,value3) == "AP":
		print "AP",
		print value3 +(value2 - value1)
	else:
		print "GP",
		print value3 * (value3/value2)
	inputs = raw_input()
	value1,value2,value3 = inputs.split()
	value1 = int(value1)
	value2 = int(value2)
	value3 = int(value3)