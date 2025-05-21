nums = [int(input()) for _ in range(3)]
a, b, c = nums
result = [0 for _ in range(10)]
temp = str(a * b * c)

for s in temp:
    n = int(s)
    result[n] += 1

for r in result:
    print(r)
