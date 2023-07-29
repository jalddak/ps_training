# BFS

from collections import deque

t = int(input())

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(t):
    l = int(input())
    visited = [[False for _ in range(l)] for _ in range(l)]
    y, x = list(map(int, input().split()))
    ry, rx = list(map(int, input().split()))
    visited[y][x] = True
    queue = deque([[y, x, 0]])
    result = 0
    while len(queue) != 0:
        y, x, cnt = queue.popleft()
        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < l and 0 <= nx < l and not visited[ny][nx]:
                if ny == ry and nx == rx:
                    queue.clear()
                    result = cnt + 1
                    break
                visited[ny][nx] = True
                queue.append([ny, nx, cnt+1])
    print(result)