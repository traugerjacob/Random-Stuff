import math

def isPrime(x):
	for i in xrange(2,int(math.sqrt(x))+1):
		if x%i==0:
			return False
	return True


a=600851475143
b=[]
for i in xrange(1,int(math.sqrt(a))+1):
	if a%i==0:
		b.append(i)
		b.append(a/i)
maxx=-1
for i in b:
	if(isPrime(i) and i>maxx):
		maxx=i
print maxx
	

