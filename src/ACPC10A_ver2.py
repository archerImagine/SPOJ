# SOPJ: http://www.spoj.com/problems/ACPC10A/
test = raw_input()
test = test.split()
x = [int(i) for i in test]

while not(x[0] == 0 and x[1] == 0 and x[2] == 0):
	if (x[2] - x[1]) == (x[1] - x[0]):
		print "AP",
		print x[2] + (x[2] - x[1])
	else:
		print "GP",
		print x[2] * x[2]/x[1]

	test = raw_input()
	test = test.split()
	x = [int(i) for i in test]


# while True:
# 	test = raw_input()
# 	test = test.split()
# 	x = [int(i) for i in test]

# 	if x[0] == 0 and x[1] == 0 and x[2] == 0:
# 		print "Hello 1"
# 		break
# 	if (x[2] - x[1]) == (x[1] - x[0]):
# 		print "AP",
# 		print x[2] + (x[2] - x[1])
# 	else:
# 		print "GP",
# 		print x[2] * x[2]/x[1]


	
