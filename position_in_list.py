# считывает список чисел 𝑙𝑠𝑡 из первой строки и число 𝑥 из второй строки, которая
# выводит все позиции, на которых встречается число 𝑥 в переданном списке 𝑙𝑠𝑡.

lst = [int(i) for i in input().split()]
x = int(input())
res = ""

for i in range(len(lst)):
	if x == lst[i]:
		res += str(i) + ' '

if len(res) == 0:
	res = "Отсутствует"

print(res)
