from collections import deque

def solution(board):
    answer = -1
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    n, m = len(board), len(board[0])
    
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                queue.append((i, j, 0))
                visited[i][j] = True
                
    while queue:
        y, x, cnt = queue.popleft()
        if board[y][x] == 'G':
            answer = cnt
            break
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            while 0<=ny<n and 0<=nx<m and board[ny][nx] != 'D':
                ny += dy[d]
                nx += dx[d]
            ny -= dy[d]
            nx -= dx[d]
            if not visited[ny][nx]:
                queue.append((ny, nx, cnt+1))
                visited[ny][nx] = True
    
    return answer