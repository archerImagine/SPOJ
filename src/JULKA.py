# http://www.spoj.com/problems/JULKA/
# all it took is to hardcode testCase = 10
# https://github.com/sarupbanskota/SPOJ/blob/master/JULKA.py
# Current world rank: #20522
testCases = 10
while testCases:
	noOfApplesTogether = int(raw_input())
	noOfApplesMoreKlaudi = int(raw_input())

	#shareOfNatalia = (noOfApplesTogether - noOfApplesMoreKlaudi)/2
	#shareOfKlaudia = (noOfApplesTogether + noOfApplesMoreKlaudi)/2

	print (noOfApplesTogether + noOfApplesMoreKlaudi)/2
	print (noOfApplesTogether - noOfApplesMoreKlaudi)/2

	testCases -= 1
