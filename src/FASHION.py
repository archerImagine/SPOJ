# SPOJ: http://www.spoj.com/problems/FASHION/
# http://stackoverflow.com/questions/11344827/summing-elements-in-a-list
# http://stackoverflow.com/questions/10271484/python-element-wise-multiplication-of-two-lists
# Current world rank: #20523
inputs = int(raw_input())
while inputs:
	noOfSamples = int(raw_input())
	mensSample = raw_input()
	womenSample = raw_input()
	
	mensSample = mensSample.split()
	mensSample = [int(i) for i in mensSample]

	womenSample = womenSample.split()
	womenSample = [int(i) for i in womenSample]

	mensSample.sort()
	womenSample.sort()

	print sum([a*b for a,b in zip(mensSample,womenSample)]) 

	inputs -= 1
