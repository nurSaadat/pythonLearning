with open('output.txt') as inf:
	string = inf.readline().strip().split(';')
	d = {}
	lst = []
	key = ''
	while len(string) > 1:
		for i in range(len(string)):
			if i == 0:
				lst.append(string[i])
				key = string[i]
				d[key] = []
			else:
				d[key].append(string[i])	
		string = inf.readline().strip().split(';')
	num1 = 0
	sum1 = 0
	sum2 = 0
	sum3 = 0
	with open('output.txt', 'w') as ouf:
		for key in lst:
			num1 += 1
			_sum = 0
			num = 0
			value = d.get(key)
			for item in range(len(value)):
				_sum += int(value[item])
				num += 1
				if item == 0:
					sum1 += int(value[item])
				elif item == 1:
					sum2 += int(value[item])
				elif item == 2:
					sum3 += int(value[item])
			ouf.write(str(_sum / num) + '\n')
		ouf.write(str(sum1 / num1) + ' ' + str(sum2 / num1) + ' ' + str(sum3 / num1) + '\n')
