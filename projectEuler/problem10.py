import math

def isPrime(x):
	for i in xrange(2,int(math.sqrt(x))+1):
		if x%i==0:
			return False
	return True

summ=-1
for i in xrange(2000000):
	if isPrime(i):
		summ+=i
print summ
