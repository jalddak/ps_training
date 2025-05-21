n = int(input())
ts = list(map(int, input().split()))
y = 0
m = 0
for t in ts:
    y += t // 30 * 10
    m += t // 60 * 15
    y += 10
    m += 15


if y < m:
    print("Y " + str(y))
elif y > m:
    print("M " + str(m))
else:
    print("Y M " + str(y))