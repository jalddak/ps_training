dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def get_portal(board, N):
    d = {}
    for i in range(N):
        for j in range(N):
            if board[i][j] > 5:
                d[board[i][j]] = d.get(board[i][j], [])
                d[board[i][j]].append((i, j))
    portal = {}
    for k in d:
        portal[d[k][0]] = d[k][1]
        portal[d[k][1]] = d[k][0]
    return portal


def calc_score(board, N, y, x, d, portal):
    sy, sx = y, x
    result = 0

    while True:
        y += dy[d]
        x += dx[d]
        if not (0 <= y < N and 0 <= x < N) or board[y][x] == 5:
            d = d+2 if d < 2 else d-2
            result += 1
        elif board[y][x] == -1:
            break
        elif 1 <= board[y][x] <= 4:
            if board[y][x] == 1:
                if d in [0, 1]:
                    d = d+2 if d < 2 else d-2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 0
            elif board[y][x] == 2:
                if d in [1, 2]:
                    d = d+2 if d < 2 else d-2
                elif d == 0:
                    d = 1
                elif d == 3:
                    d = 2
            elif board[y][x] == 3:
                if d in [2, 3]:
                    d = d+2 if d < 2 else d-2
                elif d == 1:
                    d = 2
                elif d == 0:
                    d = 3
            elif board[y][x] == 4:
                if d in [3, 0]:
                    d = d+2 if d < 2 else d-2
                elif d == 2:
                    d = 3
                elif d == 1:
                    d = 0
            result += 1

        elif 6 <= board[y][x] <= 10:
            y, x = portal[(y, x)]

        if (y, x) == (sy, sx):
            break
    return result


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    answer = 0
    board = [list(map(int, input().split())) for _ in range(N)]
    portal = get_portal(board, N)
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            for d in range(4):
                ny = i+dy[d]
                nx = j+dx[d]
                if 0<=ny<N and 0<=nx<N and board[ny][nx] == -1:
                    continue
                answer = max(answer, calc_score(board, N, i, j, d, portal))

    print("#" + str(t) + " " + str(answer))