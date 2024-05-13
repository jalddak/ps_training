from collections import deque

def solution(maps):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    loca = deque([(0, 0, 1)])
    visited[0][0] = True
    while loca:
        y, x, cnt = loca.popleft()
        if y == n-1 and x == m-1:
            return cnt
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<=ny<n and 0<=nx<m and maps[ny][nx] != 0 and not visited[ny][nx]:
                loca.append((ny, nx, cnt+1))
                visited[ny][nx] = True
    return -1