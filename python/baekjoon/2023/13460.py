# 좌표를 기록해놓으면, board를 일일이 수정할 필요가 없다는 것을 알게됨.
from collections import deque

def make_board():
    row_col = input().split()
    row_len = int(row_col[0])
    col_len = int(row_col[1])
    board = [['' for _ in range(col_len)] for _ in range(row_len)]
    visited = [[[[0 for _ in range(col_len)] for _ in range(row_len)] for _ in range(col_len)] for _ in range(row_len)]
    for i in range(row_len):
        row = input()
        for j in range(col_len):
            board[i][j] = row[j]
            if row[j] == 'R':
                ry, rx = i, j
            if row[j] == 'B':
                by, bx = i, j
    return board, visited, ry, rx, by, bx

def move(board, y, x, dy, dx):
    cnt = 0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt

def main():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    board, visited, ry, rx, by, bx = make_board()
    queue = deque([[ry, rx, by, bx, 1]])
    while len(queue) != 0:
        ry, rx, by, bx, result = queue.popleft()
        visited[ry][rx][by][bx] = 1
        if result > 10:
            print(-1)
            return -1
        for i in range(4):
            next_ry, next_rx, rcnt = move(board, ry, rx, dy[i], dx[i])
            next_by, next_bx, bcnt = move(board, by, bx, dy[i], dx[i])
            if board[next_by][next_bx] != 'O':
                if board[next_ry][next_rx] == 'O':
                    print(result)
                    return result
                if next_by == next_ry and next_bx == next_rx:
                    if rcnt > bcnt:
                        next_ry -= dy[i]
                        next_rx -= dx[i]
                    else:
                        next_by -= dy[i]
                        next_bx -= dx[i]
                if visited[next_ry][next_rx][next_by][next_bx] != 1:
                    queue.append([next_ry, next_rx, next_by, next_bx, result+1])
                    visited[next_ry][next_rx][next_by][next_bx] = 1

    print(-1)
    return -1



if __name__ == '__main__':
    main()