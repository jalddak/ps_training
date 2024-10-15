n = 1
for _ in range(3):
    n *= int(input())

sn = str(n)
check = [0 for _ in range(10)]
for c in sn:
    check[int(c)] += 1

for num in check:
    print(num)