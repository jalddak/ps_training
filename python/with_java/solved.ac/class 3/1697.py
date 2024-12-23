n, k = map(int, input().split())

if n == k:
    print(0)
    exit()

row = [1e9 for _ in range(100001)]
row[n] = 0

from collections import deque

q = deque([(n, 0)])
while q:
    x, t = q.popleft()
    nxs = [x-1, x+1, 2 * x]
    nt = t + 1
    for nx in nxs:
        if 0 <= nx <= 100000 and row[nx] > nt:
            row[nx] = nt
            q.append((nx, nt))
        if nx == k:
            print(nt)
            exit()