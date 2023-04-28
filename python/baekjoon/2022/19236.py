from collections import deque

def fish_move(board, fish_location, dy, dx):
    for key in fish_location:
        if len(fish_location[key]) == 0 or key == 17:
            continue
        y = fish_location[key][0]
        x = fish_location[key][1]

        while True:
            change_y = y + dy[board[y][x][1]]
            change_x = x + dx[board[y][x][1]]
            if change_y < 0 or change_y > 3 or change_x < 0 or change_x > 3:
                board[y][x][1] += 1
                if board[y][x][1] > 7:
                    board[y][x][1] -= 8
                continue
            else:
                if board[change_y][change_x][0] == 17:
                    board[y][x][1] += 1
                    if board[y][x][1] > 7:
                        board[y][x][1] -= 8
                    continue
            break
        
        fish_num = board[y][x][0]
        fish_direction = board[y][x][1]
        change_fish_num = board[change_y][change_x][0]
        change_fish_direction = board[change_y][change_x][1]

        board[change_y][change_x][0] = fish_num
        board[change_y][change_x][1] = fish_direction
        board[y][x][0] = change_fish_num
        board[y][x][1] = change_fish_direction

        fish_location[fish_num] = (change_y, change_x)
        if change_fish_num != 0:
            fish_location[change_fish_num] = (y, x)


def shark_move(board, fish_location, dy, dx, now_result, max_result):
    y = fish_location[17][0]
    x = fish_location[17][1]
    shark_direction = board[y][x][1]
    eat_y = y
    eat_x = x

    while True:
        eat_y = eat_y + dy[shark_direction]
        eat_x = eat_x + dx[shark_direction]
        board_copy = [[item[:] for item in board_row] for board_row in board]
        now_result_copy = now_result
        if eat_y >= 0 and eat_y < 4 and eat_x >= 0 and eat_x < 4:
            if board_copy[eat_y][eat_x][0] == 0:
                continue
            fish_location_copy = dict(list(fish_location.items())[:])
            now_result_copy += board_copy[eat_y][eat_x][0]
            max_result = max(now_result_copy, max_result)
            fish_location_copy[board_copy[eat_y][eat_x][0]] = tuple()
            board_copy[y][x][0] = 0
            fish_location_copy[17] = (eat_y,eat_x)
            board_copy[eat_y][eat_x][0] = 17
            fish_move(board_copy, fish_location_copy, dy, dx)
            max_result = shark_move(board_copy, fish_location_copy, dy, dx, now_result_copy, max_result)
        else:
            break
    return max_result

def main():
    board = [[[] for _ in range(4)] for _ in range(4)]
    fish_location = {}
    for i in range(4):
        row_info = deque(list(map(int, input().split())))
        for j in range(4):
            fish_num = row_info.popleft()
            fish_direction = row_info.popleft()-1
            fish_location[fish_num] = (i,j)
            board[i][j].append(fish_num)
            board[i][j].append(fish_direction)
    fish_location = dict(sorted(fish_location.items(), key = lambda x: x[0]))
    
    # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]

    # 상어 : 17
    result = 0
    result += board[0][0][0]
    fish_location[board[0][0][0]] = tuple()
    fish_location[17] = (0,0)
    board[0][0][0] = 17
    fish_move(board, fish_location, dy, dx)
    max_result = shark_move(board, fish_location, dy, dx, result, result)
    print(max_result)
    return 0


if __name__ == '__main__':
    main()