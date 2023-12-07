import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1] = [1, 0, 0]

dy = [0, 1, 1]
dx = [1, 0, 1]

for y in range(N):
    for x in range(N):
        if sum(dp[y][x]) == 0:
            continue
        for i in range(len(dp[y][x])):
            for d in range(3):
                if i != d and d != 2 and i != 2:
                    continue
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    if board[ny][nx] == 1:
                        continue
                    if d == 2 and (board[y+1][x] == 1 or board[y][x+1] == 1):
                        continue
                    dp[ny][nx][d] += dp[y][x][i]

print(sum(dp[N-1][N-1]))

# 시간초과
import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 1, 1]
dx = [1, 0, 1]

# 상태 : 0, 1, 2 : 가로 세로 대각선
queue = deque([[0, 0, 1]])

result = 0
while len(queue) != 0:
    state, y, x = queue.popleft()
    if (y, x) == (N-1, N-1):
        result += 1
    for d in range(3):
        if state != d and d != 2 and state != 2:
            continue
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < N:
            if board[ny][nx] == 1:
                continue
            if d == 2 and (board[y+1][x] == 1 or board[y][x+1] == 1):
                continue
            queue.append([d, ny, nx])

print(result)