a, b, c, d = int(input()), int(input()), int(input()), int(input())

print("\t", end = '')
for i in range(c,d + 1):
    print(str(i) + "\t", end = '')
print()

for i in range(a,b + 1):
    print(str(i) + "\t", end = '')
    for j in range(c,d + 1):
        print(str(j * i) + "\t", end = '')
    print()
