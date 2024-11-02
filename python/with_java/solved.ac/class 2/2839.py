n = int(input())

a1 = n // 5
x = n % 5

while a1 > -1 and x % 3 != 0:
    a1 -= 1
    x += 5

if a1 == -1:
    print(-1)
else:
    print(a1 + x // 3)