for _ in range(int(raw_input())):
	n=int(raw_input())
	if n==1:
		print "1"
	else:
		a = (n*(n+1)*2**(n - 2))
		print a
