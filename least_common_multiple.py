a, b = int(input()), int(input())

if a >= b:
    c = a
    d = b
else:
    c = b
    d = a
    
i = 1
helper = c

while c % d != 0:
    c = helper * i
    i += 1

print(c)
