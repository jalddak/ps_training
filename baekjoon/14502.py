def make_board():
    row, col = map(int, input().split())
    board = [[0 for _ in range(col)] for _ in range(row)]
    return board


def make_wall(board, num):
    num += 1
    board_copy = []
    visited = []
    for i in range(len(board)):
        board_row_copy = board[i][:]
        board_copy.append(board_row_copy)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board_copy[i][j] == 0 and [i,j] not in visited:
                board_copy[i][j] = 1
                visited.append([i,j])
                if num != 3:
                    make_wall(board_copy, num)
                    board_copy[i][j] = 0


def main():
    board = make_board()
    make_wall(board, 0)

if __name__ == '__main__':
    main()