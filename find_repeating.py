s = [int(i) for i in input().split()]
s.sort()
count = 1
res = ""
for i in range(len(s)):
	if s[i - 1] != s[i]:
		continue
	else:
		res += str(s[i]) + ' '
print(res) 
