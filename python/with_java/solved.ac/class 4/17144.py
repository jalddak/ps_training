r, c, t = map(int, input().split())

board = []
airFresh = []
for i in range(r):
    board.append(list(map(int, input().split())))
    for j in range(c):
        if board[i][j] == -1:
            airFresh.append(i)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def spread():
    temp = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] <= 0:
                continue
            amount = board[i][j] // 5
            if amount == 0:
                continue
            for d in range(4):
                ny = i + dy[d]
                nx = j + dx[d]
                if ny >= r or ny < 0 or nx >= c or nx < 0 or board[ny][nx] < 0:
                    continue
                temp[ny][nx] += amount
                board[i][j] -= amount
    
    for i in range(r):
        for j in range(c):
            board[i][j] += temp[i][j]


def clean():
    for i in range(airFresh[0]-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(c-1):
        board[0][i] = board[0][i+1]
    for i in range(airFresh[0]):
        board[i][c-1] = board[i+1][c-1]
    for i in range(c-1, 1, -1):
        board[airFresh[0]][i] = board[airFresh[0]][i-1]

    board[airFresh[0]][1] = 0

    for i in range(airFresh[1]+1, r-1):
        board[i][0] = board[i+1][0]
    for i in range(c-1):
        board[r-1][i] = board[r-1][i+1]
    for i in range(r-1, airFresh[1], -1):
        board[i][c-1] = board[i-1][c-1]
    for i in range(c-1, 1, -1):
        board[airFresh[1]][i] = board[airFresh[1]][i-1]

    board[airFresh[1]][1] = 0

for _ in range(t):
    spread()
    clean()

answer = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            answer += board[i][j]

print(answer)