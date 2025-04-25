import sys
input = sys.stdin.readline

t = int(input())
result = []

from collections import deque

dslr = ['D', 'S', 'L', 'R']

for _ in range(t):
    s, e = map(int, input().split())
    visited = [False for _ in range(10000)]
    visited[s] = True
    q = deque([[s, '']])

    while q:
        n, cmd = q.popleft()
        flag = False
        candidates = []
        candidates.append(n * 2 if n * 2 < 10000 else n * 2 % 10000)
        candidates.append(9999 if n - 1 < 0 else n - 1)
        candidates.append(n % 1000 * 10 + n // 1000)
        candidates.append(n % 10 * 1000 + n // 10)

        for d in range(4):
            cn = candidates[d]
            ncmd = cmd + dslr[d]
            if not visited[cn]:
                visited[cn] = True
                q.append([cn, ncmd])
            if cn == e:
                result.append(ncmd)
                flag = True
                break

        if flag:
            break

for r in result:
    print(r)