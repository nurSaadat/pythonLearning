# считывает с консоли числа (по одному в строке)
# до тех пор, пока сумма введённых чисел не будет равна 0
# и сразу после этого выводит сумму квадратов всех считанных чисел.

num = int(input())
l = []
l.append(num)

while num != 0:
	new_num = int(input())
	num += new_num
	l.append(new_num)

sumsqr = 0
for i in l:
	sumsqr += (i ** 2)
print(sumsqr)
