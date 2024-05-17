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


def calc_score(board, N, y, x, d, portal):
    sy, sx = y, x
    result = 0
    while True:
        y += dy[d]
        x += dx[d]
        if y < 0 or y >= N or x < 0 or x >= N:
            d = change_dir[5][d]
            result += 1
        elif board[y][x] == -1:
            break
        elif 1 <= board[y][x] <= 5:
            d = change_dir[board[y][x]][d]
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