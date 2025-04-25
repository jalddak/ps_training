n = int(input())
xys = []
for _ in range(n):
    xys.append(list(map(int, input().split())))

xys.append(xys[0])

plus = 0
minus = 0
for i in range(n):
    plus += xys[i][0] * xys[i+1][1]
    minus += xys[i][1] * xys[i+1][0]

result = abs(plus - minus) / 2 * 10
if result % 1 >= 0.5:
    result += 1
result = int(result) / 10
print(result)