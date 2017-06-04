import math

def sumToN(n):
	return ((n + 1)*n/2.0)

n = 1000
threes = math.floor((n-1)/3)
fives = math.floor((n-1)/5)
fifteens = math.floor((n-1)/15)

print 3 * sumToN(threes) + 5 * sumToN(fives) - 15 * sumToN(fifteens)
