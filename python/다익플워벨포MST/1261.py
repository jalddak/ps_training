M, N = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

board = [list(map(int, list(input()))) for _ in range(N)]

import heapq
heap = [(0, [0, 0])]
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0] = True

while heap:
    cost, loca = heapq.heappop(heap)
    y, x = loca
    if (y, x) == (N-1, M-1):
        print(cost)
        exit()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            heapq.heappush(heap, (cost + board[ny][nx], [ny, nx]))