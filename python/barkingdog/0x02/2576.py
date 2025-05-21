sums = 0
minN = 101
for _ in range(7):
    num = int(input())
    if num % 2 == 0:
        continue
    sums += num
    minN = min(minN, num)

if sums == 0:
    print(-1)
else:
    print(sums)
    print(minN)

