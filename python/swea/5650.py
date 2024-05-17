dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# change_dir : 실행속도 빠른 사람의 것을 참고해봄
change_dir = [{},{0:2,1:3,2:1,3:0},{0:1,1:3,2:0,3:2},{0:3,1:2,2:0,3:1},{0:2,1:0,2:3,3:1},{0:2,1:3,2:0,3:1}]


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


def plus_cnt(record, visited):
    for y, x in visited:
        record[y][x][visited[(y, x)]] += 1


def init_record(record, visited):
    for y, x in visited:
        record[y][x][visited[(y, x)]] = 0


def calc_score(board, N, y, x, d, portal, record):
    sy, sx = y, x
    visited = {(y,x) : d}
    while True:
        y += dy[d]
        x += dx[d]
        if y < 0 or y >= N or x < 0 or x >= N:
            d = change_dir[5][d]
            plus_cnt(record, visited)
        elif board[y][x] == -1:
            break
        elif board[y][x] == 0:
            if (y, x) in visited:
                del visited[(y, x)]
            if record[y][x][d] == 0:
                visited[(y, x)] = d
        elif 1 <= board[y][x] <= 5:
            d = change_dir[board[y][x]][d]
            plus_cnt(record, visited)
        elif 6 <= board[y][x] <= 10:
            y, x = portal[(y, x)]

        if (y, x) == (sy, sx):
            init_record(record, visited)
            break


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    answer = 0
    board = [list(map(int, input().split())) for _ in range(N)]
    record = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    portal = get_portal(board, N)
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            for d in range(4):
                if record[i][j][d] != 0:
                    continue
                calc_score(board, N, i, j, d, portal, record)

    answer = max([max([max(record[i][j]) for j in range(N)]) for i in range(N)])
    print("#" + str(t) + " " + str(answer))