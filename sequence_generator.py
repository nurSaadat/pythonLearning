 # выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... 
 # (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное
 # целое число n — столько элементов последовательности должна отобразить программа. 
 # На выходе ожидается последовательность чисел, записанных через пробел в одну строку. 
 
num = int(input())
out = 1
res = ""
while num > 0:
	count = 0
	while count < out:
		if num == 0:
			break
		res += (str(out) + " ")
		count += 1
		num -= 1
	out += 1

print(res)
