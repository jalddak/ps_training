n = int(input())

board = [list(map(lambda x:abs(x-1), map(int, list(input())))) for _ in range(n)]

from collections import deque

queue = deque([[0, 0, 0]])
visited = [[n*n for _ in range(n)] for _ in range(n)]
visited[0][0] = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while queue:
    y, x, cnt = queue.popleft()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < n and 0 <= nx < n and cnt < visited[ny][nx]:
            ncnt = cnt + board[ny][nx]
            visited[ny][nx] = ncnt
            queue.append([ny, nx, ncnt])

print(visited[n-1][n-1])


n = int(input())

board = [list(map(lambda x:abs(x-1), map(int, list(input())))) for _ in range(n)]

import heapq
heap = [(0, [0, 0])]
visited = [[n*n for _ in range(n)] for _ in range(n)]
visited[0][0] = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while heap:
    cnt, loca = heapq.heappop(heap)
    y, x = loca
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < n and 0 <= nx < n and cnt < visited[ny][nx]:
            ncnt = cnt + board[ny][nx]
            visited[ny][nx] = ncnt
            heapq.heappush(heap, (ncnt, [ny, nx]))

print(visited[n-1][n-1])