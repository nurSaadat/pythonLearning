# В институте биоинформатики по офису передвигается робот. 
# Недавно студенты из группы программистов написали для него программу,
# по которой робот, когда заходит в комнату, считает количество программистов в ней 
# и произносит его вслух: "n программистов".

x = int(input())
c = x % 100
d = x % 10
if 0 <= x <= 1000:
    if c == 11 or c == 12 or c == 13 or c == 14:
        print(str(x) + " программистов")
    elif  d == 1:
        print(str(x) + " программист")
    elif d == 2 or d == 3 or d == 4:
        print(str(x) + " программиста")
    else: 
        print(str(x) + " программистов")
