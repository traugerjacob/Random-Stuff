import sys.argv
def maxLenSubstring(string, size):
	best = 0
	current = {}
	running = ""
	for i in range(len(string)):
		if string[i] in current:
			running += string[i]
			current[string[i]] = i
			if len(running) > best:
				best = len(running)
		else:
			if len(current) < size:
				current[string[i]] = i
				running += string[i]
				if len(running) > best:
					best = len(running)
			else:
				if len(running) > best:
					best = len(running)
				first = current[running[0]]
				for j in current.keys():
					if current[j] <= first:
						del current[j]
				running = running[first+1:] +  string[i]
				current[string[i]] = 1
	return best

print maxLenSubstring("A man a plan a canal, panama!", 6)
		
