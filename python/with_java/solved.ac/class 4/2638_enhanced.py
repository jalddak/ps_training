n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

import heapq
heap = [(0, 0, 0)]
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True
checked = [[0 for _ in range(m)] for _ in range(n)]

answer = 0
while(heap):
    t, y, x = heapq.heappop(heap)
    answer = max(answer, t)
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        nt = t
        if ny >= n or ny < 0 or nx >= m or nx < 0 or visited[ny][nx]:
            continue
        if board[ny][nx] == 1:
            checked[ny][nx] += 1
            if checked[ny][nx] < 2:
                continue
            nt = t + 1
        visited[ny][nx] = True
        heapq.heappush(heap, (nt, ny, nx))

print(answer)