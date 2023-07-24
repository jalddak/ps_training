# BFS

from collections import deque

N, K = list(map(int, input().split()))

visited = [False for _ in range(100001)]

queue = deque([[N, 0]])

while len(queue) != 0:
    loca, cnt = queue.popleft()
    if loca == K:
        print(cnt)
        exit()
    if 0 <= loca < 100001 and not visited[loca]:
        visited[loca] = True
        candidate = [loca-1, loca+1, 2*loca]
        for l in candidate:
            if l == K:
                print(cnt+1)
                exit()
            queue.append([l, cnt+1])