phi = (1 + 5 ** .5) / 2
n = 10#4000000

ret = 0

for i in xrange(0, n, 3):
	ret += ((phi ** i) - ((-phi) ** (-i))) / (5 ** .5)
print ret
