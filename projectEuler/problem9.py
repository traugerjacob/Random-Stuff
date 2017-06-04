def problem9():
	for a in xrange(500):
		for b in xrange(a+1,500):
			c=1000-a-b
			if(a*a+b*b==c*c):
				return a*b*c
print problem9()
