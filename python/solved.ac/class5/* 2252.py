# 위상정렬

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

Vlist = [[0, []] for _ in range(N)]
for _ in range(M):
    t, s = map(lambda x:x-1, map(int, input().split()))
    Vlist[t][1].append(s)
    Vlist[s][0] += 1

from collections import deque
queue = deque([])
for i in range(N):
    if Vlist[i][0] == 0:
        queue.append(i)

result = []
while len(queue) != 0:
    n = queue.popleft()
    for check in Vlist[n][1]:
        Vlist[check][0] -= 1
        if Vlist[check][0] == 0:
            queue.append(check)
    result.append(n+1)

result = map(str, result)
print(' '.join(result))