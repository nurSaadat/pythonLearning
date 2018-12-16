with open('output.txt') as inf:
	res = ''
	helper = ''
	ch = ''
	s1 = inf.readline()
	
	for i in s1: 
		if ch == '':
			ch += i
		elif '0' <= i <= '9':
			helper += i
		elif helper != '' or i == '\n':
			res += ch * int(helper)
			ch = ''
			helper = ""
			ch += i
	with open('output.txt', 'w') as ouf:
		ouf.write(res + '\n')
