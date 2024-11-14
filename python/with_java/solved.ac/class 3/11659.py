import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
ps = [0]
for i in range(n):
    ps.append(ps[i] + nums[i])

for _ in range(m):
    l, r = map(int, input().split())
    print(ps[r] - ps[l-1])