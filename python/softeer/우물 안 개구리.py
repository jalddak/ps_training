import sys

n, m = map(int, input().split())
bests = [i for i in range(n+1)]
weights = [0] + list(map(int, input().split()))

for _ in range(m):
    f, s = map(int, input().split())
    if weights[bests[f]] <= weights[s]:
        bests[f] = s
    if weights[bests[s]] <= weights[f]:
        bests[s] = f

cnt = 0
for i in range(1, n+1):
    if i == bests[i]:
        cnt += 1

print(cnt)