string = input().lower()
d = {}
for word in string.split():
	if word not in d.keys():
		d[word] = 1
	else:
		d[word] += 1
for key,value in d.items():
	print(key, value)
