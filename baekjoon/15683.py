from collections import deque

def make_board():
    row, col = map(int, input().split())
    board = [[0 for _ in range(col)] for _ in range(row)]
    cctv_location = deque([])
    for i in range(row):
        board_row = list(map(int, input().split()))
        for j in range(col):
            board[i][j] = board_row[j]
            if board_row[j] > 0 and board_row[j] < 6:
                cctv_location.append((i,j))

    return board, cctv_location


def up(board, y, x):
    i = y - 1
    while i >= 0:
            if board[i][x] == 6:
                break
            elif board[i][x] == 0:
                board[i][x] = '#'
            i -= 1


def down(board, y, x):
    i = y + 1
    while i < len(board):
        if board[i][x] == 6:
            break
        elif board[i][x] == 0:
            board[i][x] = '#'
        i += 1


def left(board, y, x):
    i = x - 1
    while i >= 0:
            if board[y][i] == 6:
                break
            elif board[y][i] == 0:
                board[y][i] = '#'
            i -= 1


def right(board, y, x):
    i = x + 1
    while i < len(board[y]):
        if board[y][i] == 6:
            break
        elif board[y][i] == 0:
            board[y][i] = '#'
        i += 1


def check(board, cctv, board_list):
    y = cctv[0]
    x = cctv[1]
    board_copy = [[b for b in board[i]] for i in range(len(board))]
    if board[y][x] == 1:
        up(board_copy, y, x)
        board_list.append(board_copy)
        board_copy = [[b for b in board[i]] for i in range(len(board))]
        down(board_copy, y, x)
        board_list.append(board_copy)
        board_copy = [[b for b in board[i]] for i in range(len(board))]
        left(board_copy, y, x)
        board_list.append(board_copy)
        board_copy = [[b for b in board[i]] for i in range(len(board))]
        right(board_copy, y, x)
        board_list.append(board_copy)
    elif board[y][x] == 2:
        up(board_copy, y, x)
        down(board_copy, y, x)
        board_list.append(board_copy)
        board_copy = [[b for b in board[i]] for i in range(len(board))]
        left(board_copy, y, x)
        right(board_copy, y, x)
        board_list.append(board_copy)
    elif board[y][x] == 3:
        up(board_copy, y, x)
        right(board_copy, y, x)
        board_list.append(board_copy)
        board_copy = [[b for b in board[i]] for i in range(len(board))]
        right(board_copy, y, x)
        down(board_copy, y, x)
        board_list.append(board_copy)
        board_copy = [[b for b in board[i]] for i in range(len(board))]
        down(board_copy, y, x)
        left(board_copy, y, x)
        board_list.append(board_copy)
        board_copy = [[b for b in board[i]] for i in range(len(board))]
        left(board_copy, y, x)
        up(board_copy, y, x)
        board_list.append(board_copy)
    elif board[y][x] == 4:
        left(board_copy, y, x)
        up(board_copy, y, x)
        right(board_copy, y, x)
        board_list.append(board_copy)
        board_copy = [[b for b in board[i]] for i in range(len(board))]
        up(board_copy, y, x)
        right(board_copy, y, x)
        down(board_copy, y, x)
        board_list.append(board_copy)
        board_copy = [[b for b in board[i]] for i in range(len(board))]
        right(board_copy, y, x)
        down(board_copy, y, x)
        left(board_copy, y, x)
        board_list.append(board_copy)
        board_copy = [[b for b in board[i]] for i in range(len(board))]
        down(board_copy, y, x)
        left(board_copy, y, x)
        up(board_copy, y, x)
        board_list.append(board_copy)
    elif board[y][x] == 5:
        up(board_copy, y, x)
        right(board_copy, y, x)
        down(board_copy, y, x)
        left(board_copy, y, x)
        board_list.append(board_copy)


def main():
    board, cctv_location = make_board()
    board_list = deque([board])
    for i in range(len(cctv_location)):
        cctv = cctv_location.popleft()
        before_len = len(board_list)
        for j in range(before_len):
            board = board_list.popleft()
            check(board, cctv, board_list)
    min_blind = len(board) * len(board[0])
    for i in range(len(board_list)):
        blind_spot = 0
        for j in range(len(board_list[i])):
            for k in range(len(board_list[i][j])):
                if board_list[i][j][k] == 0:
                    blind_spot += 1
        min_blind = min(min_blind, blind_spot)
    print(min_blind)
    return min_blind


if __name__ == '__main__':
    main()