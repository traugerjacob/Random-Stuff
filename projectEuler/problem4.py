def problem4():
	maxx=-1
	for i in xrange(100,1000):
		for x in xrange(100,1000):
			b=i*x
			if(isPalindrome(str(b)) and b>maxx):
				maxx=b
	return maxx

def isPalindrome(x):
	for i in xrange(int(len(x)/2)):
		if x[i]!=x[len(x)-i-1]:
			return False
	return True
print problem4()
