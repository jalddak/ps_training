import re

def make_board():
    row_col = input("row and col : ").split()
    row = int(row_col[0])
    col = int(row_col[1])
    board = [['' for _ in range(col)] for _ in range(row)]
    R_location = [0,0]
    for i in range(row):
        real_row = input()
        for j in range(col):
            board[i][j] = real_row[j]
            if real_row[j] == 'R':
                R_location = [i,j]
            if real_row[j] == 'B':
                B_location = [i,j]
    return board, R_location, B_location


def move(board, R_location, B_location, back_move, result):
    result += 1
    if result > 10:
        return result

    R_x, R_y, B_x, B_y = R_location[1], R_location[0], B_location[1], B_location[0]
    up_R, up_B = R_y, B_y
    down_R, down_B = R_y, B_y
    left_R, left_B = R_x, B_x
    right_R, right_B = R_x, B_x

    possible = []
    if board[R_y - 1][R_x] != '#' or board[B_y - 1][B_x] != '#':
        possible.append('up')
    if board[R_y + 1][R_x] != '#' or board[B_y + 1][B_x] != '#':
        possible.append('down')
    if board[R_y][R_x - 1] != '#' or board[B_y][B_x - 1] != '#':
        possible.append('left')
    if board[R_y][R_x + 1] != '#' or board[B_y][B_x + 1] != '#':
        possible.append('right')
    
    if back_move in possible:
        possible.remove(back_move)
    result_list = []
    print(possible)
    for i  in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = '')
        print()
    print()
    for p in possible:
        board_copy = []
        for i in range(len(board)):
            board_copy_row = []
            for j in range(len(board[i])):
                board_copy_row.append(board[i][j])
            board_copy.append(board_copy_row)
                
        if p == 'up':
            while board_copy[up_R - 1][R_x] == '.':
                board_copy[up_R][R_x] = '.'
                up_R = up_R - 1
                board_copy[up_R][R_x] = 'R'
            if board_copy[up_R - 1][R_x] == 'O':
                board_copy[up_R][R_x] = '.'

            while board_copy[up_B - 1][B_x] == '.':
                board_copy[up_B][B_x] = '.'
                up_B = up_B - 1
                board_copy[up_B][B_x] = 'B'
            if board_copy[up_B - 1][B_x] == 'O':
                continue

            while board_copy[up_R - 1][R_x] == '.':
                board_copy[up_R][R_x] = '.'
                up_R = up_R - 1
                board_copy[up_R][R_x] = 'R'
            if board_copy[up_R - 1][R_x] == 'O':
                board_copy[up_R][R_x] = '.'
                return result
            else:
                result_list.append(move(board_copy, [up_R, R_x], [up_B, B_x], 'down', result))

        elif p == 'down':
            while board_copy[down_R + 1][R_x] == '.':
                board_copy[down_R][R_x] = '.'
                down_R = down_R + 1
                board_copy[down_R][R_x] = 'R'
            if board_copy[down_R + 1][R_x] == 'O':
                board_copy[down_R][R_x] = '.'

            while board_copy[down_B + 1][B_x] == '.':
                board_copy[down_B][B_x] = '.'
                down_B = down_B + 1
                board_copy[down_B][B_x] = 'B'
            if board_copy[down_B + 1][B_x] == 'O':
                continue

            while board_copy[down_R + 1][R_x] == '.':
                board_copy[down_R][R_x] = '.'
                down_R = down_R + 1
                board_copy[down_R][R_x] = 'R'
            if board_copy[down_R + 1][R_x] == 'O':
                board_copy[down_R][R_x] = '.'
                return result
            else:
                result_list.append(move(board_copy, [down_R, R_x], [down_B, B_x], 'up', result))

        elif p == 'left':
            while board_copy[R_y][left_R - 1] == '.':
                board_copy[R_y][left_R] = '.'
                left_R = left_R - 1
                board_copy[R_y][left_R] = 'R'
            if board_copy[R_y][left_R - 1] == 'O':
                board_copy[R_y][left_R] = '.'

            while board_copy[B_y][left_B - 1] == '.':
                board_copy[B_y][left_B] = '.'
                left_B = left_B - 1
                board_copy[B_y][left_B] = 'B'
            if board_copy[B_y][left_B - 1] == 'O':
                continue

            while board_copy[R_y][left_R - 1] == '.':
                board_copy[R_y][left_R] = '.'
                left_R = left_R - 1
                board_copy[R_y][left_R] = 'R'
            if board_copy[R_y][left_R - 1] == 'O':
                board_copy[R_y][left_R] = '.'
                return result
            else:
                result_list.append(move(board_copy, [R_y, left_R], [B_y, left_B], 'right', result))

        elif p == 'right':
            while board_copy[R_y][right_R + 1] == '.':
                board_copy[R_y][right_R] = '.'
                right_R = right_R + 1
                board_copy[R_y][right_R] = 'R'
            if board_copy[R_y][right_R + 1] == 'O':
                board_copy[R_y][right_R] = '.'

            while board_copy[B_y][right_B + 1] == '.':
                board_copy[B_y][right_B] = '.'
                right_B = right_B + 1
                board_copy[B_y][right_B] = 'B'
            if board_copy[B_y][right_B + 1] == 'O':
                continue

            while board_copy[R_y][right_R + 1] == '.':
                board_copy[R_y][right_R] = '.'
                right_R = right_R + 1
                board_copy[R_y][right_R] = 'R'
            if board_copy[R_y][right_R + 1] == 'O':
                board_copy[R_y][right_R] = '.'
                return result
            else:
                result_list.append(move(board_copy, [R_y, right_R], [B_y, right_B], 'right', result))
    if len(result_list) == 0:
        return 11
    else:
        return min(result_list)



def main():
    board, R_location, B_location = make_board()
    result = 0
    result = move(board, R_location, B_location, 'Nope', result)
    if result > 10:
        return -1
    else:
        return result


if __name__ == '__main__':
    main()