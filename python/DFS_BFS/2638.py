N, M = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 외부 = 9
# 치즈 2,3,4,5 = 주변에 외부공기 닿는 변 개수 +1

stack = [[0, 0]]
board[0][0] = 9
while len(stack) != 0:
    y, x = stack.pop()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if board[ny][nx] == 0:
                stack.append([ny, nx])
                board[ny][nx] = 9
            elif 0 < board[ny][nx] < 9:
                board[ny][nx] += 1

time = 0
while True:
    next = []
    for i in range(N):
        for j in range(M):
            if 2 < board[i][j] < 9:
                next.append([i, j])
                board[i][j] = 9
    if len(next) == 0:
        break
    time += 1
    while len(next) != 0:
        y, x = next.pop()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == 0:
                    next.append([ny, nx])
                    board[ny][nx] = 9
                elif 0 < board[ny][nx] < 9:
                    board[ny][nx] += 1
print(time)