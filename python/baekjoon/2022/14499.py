def make_board():
    first_row = input().split()
    first_row = list(map(int, first_row))
    board = [[0 for _ in range(first_row[1])] for _ in range(first_row[0])]
    dice_location = [first_row[2], first_row[3]]
    for i in range(first_row[0]):
        num = input().split()
        num = list(map(int, num))
        for j in range(first_row[1]):
            board[i][j] = num[j]
    return board, dice_location


def move_dice(board, dice_location):
    dx = [0, 1, -1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    move = input().split()
    move = list(map(int, move))
    dice = [[0 for _ in range(3)] for _ in range(4)]
    for m in move:
        dice_location_y = dice_location[0] + dy[m]
        dice_location_x = dice_location[1] + dx[m]
        if dice_location_y < 0 or dice_location_y > len(board) - 1 or dice_location_x < 0 or dice_location_x > len(board[0]) - 1:
            continue
        dice_location[0] = dice_location_y
        dice_location[1] = dice_location_x
        down = dice[1][1]
        if m == 1:
            dice[1][1] = dice[1][2]
            dice[1][2] = dice[3][1]
            dice[3][1] = dice[1][0]
            dice[1][0] = down

        elif m == 2:
            dice[1][1] = dice[1][0]
            dice[1][0] = dice[3][1]
            dice[3][1] = dice[1][2]
            dice[1][2] = down

        elif m == 3:
            dice[1][1] = dice[0][1]
            dice[0][1] = dice[3][1]
            dice[3][1] = dice[2][1]
            dice[2][1] = down

        elif m == 4:
            dice[1][1] = dice[2][1]
            dice[2][1] = dice[3][1]
            dice[3][1] = dice[0][1]
            dice[0][1] = down

        down = dice[1][1]
        board_num = board[dice_location[0]][dice_location[1]]
        if board_num == 0:
            board[dice_location[0]][dice_location[1]] = down
        else:
            dice[1][1] = board_num
            board[dice_location[0]][dice_location[1]] = 0

        print(dice[3][1])



def main():
    board, dice_location = make_board()
    move_dice(board, dice_location)
    return 0


if __name__ == '__main__':
    main()


    # for i in range(len(board)):
    #     for j in range(len(board[i])):
    #         print(board[i][j], end=' ')
    #     print()
    # print(dice_location)