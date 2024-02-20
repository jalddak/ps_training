import sys
input = sys.stdin.readline

n, q = map(int, input().split())
ybs = list(map(int, input().split()))
ybs.sort()
ybis = {}
cnt = 0
for yb in ybs:
    ybis[yb] = (cnt, n-cnt-1)
    cnt += 1

for _ in range(q):
    ex = int(input())
    if ex not in ybis:
        print(0)
        continue
    print(ybis[ex][0] * ybis[ex][1])
    