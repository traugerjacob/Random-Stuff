import math

def isPrime(x): 
    for i in xrange(2,int(math.sqrt(x))+1): 
        if x%i==0: 
            return False 
    return True

num=0
change=2
while num<10001:
	if isPrime(change)==True:
		num+=1
	change+=1
print change-1
