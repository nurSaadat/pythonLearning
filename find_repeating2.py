#print elements occuring more than just one time

s = [int(i) for i in input().split()]
s.sort()
count = 1
res = ""
for i in range(len(s)):
	if s[i - 1] != s[i]:
		count=1
		continue
	else:
		if count == 1:
			res += str(s[i]) + ' '
			count+=1
		else:
			continue
if len(s) == 1:
	res = ''
print(res) 
