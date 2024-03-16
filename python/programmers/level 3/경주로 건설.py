import heapq

def solution(board):
    n, m = len(board), len(board[0])
    visited = [[[-1 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    board[0][0] = 1
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    board[0][0] = 2
    heap = [(0, 0, 0, -1)]
    
    while heap:
        cost, y, x, t = heapq.heappop(heap)
        if (y, x) == (n-1, m-1):
            return cost
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            nt = d % 2
            ncost = cost
            if t == -1 or nt == t:
                ncost += 100
            else:
                ncost += 600
            if 0<=ny<n and 0<=nx<m and board[ny][nx] == 0 and (visited[ny][nx][nt] == -1 or visited[ny][nx][nt] >= ncost):
                visited[ny][nx][nt] = ncost
                heapq.heappush(heap, (ncost, ny, nx, nt))