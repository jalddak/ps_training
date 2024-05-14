def check_remain_block(board, w, h):
    result = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] != 0:
                result += 1
    return result


def fall_block(board, w, h):
    for x in range(w):
        floor = h - 1
        for y in range(floor, -1, -1):
            if board[y][x] != 0:
                board[floor][x] = board[y][x]
                if y != floor:
                    board[y][x] = 0
                floor -= 1


def break_block(board, x, w, h):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    stack = []
    for y in range(h):
        if board[y][x] == 0:
            continue
        r = board[y][x]
        board[y][x] = 0
        if r != 1:
            stack.append((y, x, r))
        break
    while stack:
        y, x, r = stack.pop()
        for d in range(4):
            for p in range(1, r):
                ny = y + dy[d] * p
                nx = x + dx[d] * p
                if 0 <= ny < h and 0 <= nx < w and board[ny][nx] != 0:
                    nr = board[ny][nx]
                    board[ny][nx] = 0
                    if nr != 1:
                        stack.append((ny, nx, nr))


def shoot(board, cnt, n, w, h, result):
    if n == cnt:
        result = min(result, check_remain_block(board, w, h))
        return result
    for x in range(w):
        nboard = [row[:] for row in board]
        break_block(nboard, x, w, h)
        fall_block(nboard, w, h)
        result = min(result, shoot(nboard, cnt + 1, n, w, h, result))
    return result


T = int(input())
for t in range(1, T + 1):
    answer = 0
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    answer = shoot(board, 0, n, w, h, w * h)
    print("#" + str(t) + " " + str(answer))
