# for every element there should be printed the sum of its neighbours

s = [int(i) for i in input().split()]
if len(s) == 1:
	print(str(s[0]))
else:
	res = ""
	for num in range(len(s)):
		if num == len(s) - 1:
			res += str(s[num - 1] + s[0])
		else:
			res += str(s[num - 1] + s[num + 1]) + ' '
	print(res)
