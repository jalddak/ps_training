import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

maxScore = 0
for i in range(n):
    maxScore = max(maxScore, max(board[i]))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

from collections import deque

answer = 0

for i in range(n):
    for j in range(m):
        q = deque()
        q.append([board[i][j], i, j, 1, 0])

        candidates = []
        while q:
            score, y, x, cnt, direction = q.popleft()

            if cnt == 4:
                answer = max(answer, score)
                continue

            if score + maxScore * (4 - cnt) < answer:
                continue

            for d in range(4):
                if cnt != 1 and direction == (d + 2 if d + 2 < 4 else d - 2):
                    continue
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < n and 0 <= nx < m:
                    ncnt = cnt + 1
                    nscore = score + board[ny][nx]
                    q.append([nscore, ny, nx, ncnt, d])
                    if cnt == 1:
                        candidates.append(board[ny][nx])

        temp = sum(candidates) + board[i][j]
        if len(candidates) == 4:
            temp -= min(candidates)
        answer = max(answer, temp)
            
print(answer)