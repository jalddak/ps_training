import sys
def input():
    return sys.stdin.readline().strip()

t = int(input())

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

from collections import deque

answer = []
for _ in range(t):
    l = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())

    visited = [[False for _ in range(l)] for _ in range(l)]
    visited[sy][sx] = True

    q = deque([(sy, sx, 0)])
    result = 0
    while q:
        y, x, cnt = q.popleft()
        if y == ey and x == ex:
            result = cnt
            break
        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny >= l or ny < 0 or nx >= l or nx < 0 or visited[ny][nx]:
                continue
            q.append((ny, nx, cnt + 1))
            visited[ny][nx] = True
    
    answer.append(result)

print("\n".join(map(str, answer)))
