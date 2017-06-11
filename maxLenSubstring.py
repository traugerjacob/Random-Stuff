#returns the longest substring where there are less than size different characters
def maxLenSubstring(string, size):
	best = 0
	current = {}
	running = ""
	for i in range(len(string)):
		if string[i] in current:
			running += string[i]
			current[string[i]] += 1
			if len(running) > best:
				best = len(running)
		else:
			if len(current) < size:
					current[string[i]] = 1
					running += string[i]
					if len(running) > best:
						best = len(running)
			else:
				if len(running) > best:
					best = len(running)

				current[string[i]] = 1
				running += string[i]
				while len(current) > size:
					first = running[0]
					running = running[1:]
					current[first] -= 1
					if current[first] == 0:
						del current[first]
	return best

#a test case
print maxLenSubstring("a man a plan a canal panama", 6)
		
