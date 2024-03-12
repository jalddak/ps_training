from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                queue.append((i, j, 0))
                visited[i][j] = True
    
    can = False
    while queue:
        y, x, cnt = queue.popleft()
        if maps[y][x] == 'L':
            answer += cnt
            queue = deque([(y, x, 0)])
            visited = [[False for _ in range(m)] for _ in range(n)]
            visited[y][x] = True
            can = True
            break
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0<=ny<n and 0<=nx<m and maps[ny][nx] != 'X' and not visited[ny][nx]:
                queue.append((ny, nx, cnt+1))
                visited[ny][nx] = True
    
    if not can:
        return -1
    
    can = False
    while queue:
        y, x, cnt = queue.popleft()
        if maps[y][x] == 'E':
            answer += cnt
            can = True
            break
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0<=ny<n and 0<=nx<m and maps[ny][nx] != 'X' and not visited[ny][nx]:
                queue.append((ny, nx, cnt+1))
                visited[ny][nx] = True
    
    if not can:
        return -1
    
    return answer