import sys
input = sys.stdin.readline

import heapq

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


results = []
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]

    heap = [(board[0][0], (0, 0))]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[0][0] = True

    while heap:
        cost, loca = heapq.heappop(heap)
        y, x = loca
        if loca == (N-1, N-1):
            results.append(cost)
            break
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = True
                heapq.heappush(heap, (cost+board[ny][nx], (ny, nx)))

for i in range(len(results)):
    print("Problem " + str(i+1) + ": " + str(results[i]))