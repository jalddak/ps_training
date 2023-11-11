N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dy = [0, -1, -1]
dx = [-1, -1, 0]

for i in range(N):
    for j in range(M):
        temp = board[i][j]
        for d in range(3):
            cy = i + dy[d]
            cx = j + dx[d]
            if 0 <= cy < N and 0 <= cx < M:
                board[i][j] = max(board[i][j], temp+board[cy][cx])

print(board[N-1][M-1])