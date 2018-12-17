with open('output.txt') as inf:
	string = inf.read().replace('\n',' ').lower()
	d = {}
	big_key = ""
	big_val = 1
	for word in string.split():
		if word not in d.keys():
			d[word] = 1
		else:
			d[word] += 1
			if d[word] > big_val:
				big_val = d[word]
				big_key = word
			elif d[word] == big_val and big_key > word:
				big_val = d[word]
				big_key = word
		
	print(big_key, big_val)
