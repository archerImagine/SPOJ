def feynman(n):
	if n == 1:
		return 1
	else:
		return (n * (n+1)*(2*n +1))/6

next = int(raw_input())
while next != 0:
	print feynman(next)
	next = int(raw_input())
	