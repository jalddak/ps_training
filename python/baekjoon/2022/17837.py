def main():
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dy = [0, 0, 0, -1, 1]
    dx = [0, 1, -1, 0, 0]
    piece = [[[] for _ in range(N)] for _ in range(N)]
    direction_list = []
    location_list = []
    for i in range(K):
        row, col, direction = map(int, input().split())
        row -= 1
        col -= 1
        piece[row][col].append(i)
        if len(piece[row][col]) >= 4:
            print(0)
            return 0
        direction_list.append(direction)
        location_list.append((row, col))
    
    turn = 0
    while turn <= 1000:
        turn += 1
        for i in range(K):
            y = location_list[i][0]
            x = location_list[i][1]
            index = piece[y][x].index(i)
            move_list = piece[y][x][index:]

            after_y = y + dy[direction_list[i]]
            after_x = x + dx[direction_list[i]]
            if after_y >= 0 and after_y < N and after_x >= 0 and after_x < N:
                if board[after_y][after_x] == 0:
                    piece[y][x] = piece[y][x][:index]
                    piece[after_y][after_x] += move_list
                    for k in move_list:
                        location_list[k] = (after_y, after_x)

                elif board[after_y][after_x] == 1:
                    move_list.reverse()
                    piece[y][x] = piece[y][x][:index]
                    piece[after_y][after_x] += move_list
                    for k in move_list:
                        location_list[k] = (after_y, after_x)
            
                elif board[after_y][after_x] == 2:
                    if direction_list[i] % 2 == 0:
                        direction_list[i] -= 1
                    else:
                        direction_list[i] += 1
                    after_y = y + dy[direction_list[i]]
                    after_x = x + dx[direction_list[i]]

                    if after_y >= 0 and after_y < N and after_x >= 0 and after_x < N:
                        if board[after_y][after_x] == 0:
                            piece[y][x] = piece[y][x][:index]
                            piece[after_y][after_x] += move_list
                            for k in move_list:
                                location_list[k] = (after_y, after_x)

                        elif board[after_y][after_x] == 1:
                            move_list.reverse()
                            piece[y][x] = piece[y][x][:index]
                            piece[after_y][after_x] += move_list
                            for k in move_list:
                                location_list[k] = (after_y, after_x)
            
            else:
                if direction_list[i] % 2 == 0:
                    direction_list[i] -= 1
                else:
                    direction_list[i] += 1
                after_y = y + dy[direction_list[i]]
                after_x = x + dx[direction_list[i]]

                if after_y >= 0 and after_y < N and after_x >= 0 and after_x < N:
                    if board[after_y][after_x] == 0:
                        piece[y][x] = piece[y][x][:index]
                        piece[after_y][after_x] += move_list
                        for k in move_list:
                            location_list[k] = (after_y, after_x)

                    elif board[after_y][after_x] == 1:
                        move_list.reverse()
                        piece[y][x] = piece[y][x][:index]
                        piece[after_y][after_x] += move_list
                        for k in move_list:
                            location_list[k] = (after_y, after_x)
            
            if after_y >= 0 and after_y < N and after_x >= 0 and after_x < N:
                if len(piece[after_y][after_x]) >= 4:
                    print(turn)
                    return turn

        for i in range(N):
            print(piece[i])         
        print()
    print(-1)
    return -1


if __name__ == '__main__':
    main()