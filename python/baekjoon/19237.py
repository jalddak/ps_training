def shark_move(N, M, k, board, shark_loca, shark_dire, shark_info, time):
    time += 1

    # 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]

    for i in range(1, len(shark_dire)+1):
        if i not in shark_loca:
            continue
        direction = shark_dire[i-1]
        priority = shark_info[i-1][direction-1]
        location_y = shark_loca[i][0]
        location_x = shark_loca[i][1]

        check_empty = 0
        for j in range(len(priority)):
            next_y = location_y + dy[priority[j]]
            next_x = location_x + dx[priority[j]]
            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
                if board[next_y][next_x][0] == 0:
                    shark_loca[i] = [next_y, next_x]
                    shark_dire[i-1] = priority[j]
                    check_empty += 1
                    break
        if check_empty == 0:
            for j in range(len(priority)):
                next_y = location_y + dy[priority[j]]
                next_x = location_x + dx[priority[j]]
                if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
                    if board[next_y][next_x][0] == i:
                        shark_loca[i] = [next_y, next_x]
                        shark_dire[i-1] = priority[j]
                        check_empty += 1
                        break

    for i in range(N):
        for j in range(N):
            if board[i][j][1] != 0:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j][0] = 0
    
    for i in range(1, len(shark_dire)+1):
        if i not in shark_loca:
            continue
        location_y = shark_loca[i][0]
        location_x = shark_loca[i][1]
        if board[location_y][location_x][0] == 0 or board[location_y][location_x][0] == i:
            board[location_y][location_x][0] = i
            board[location_y][location_x][1] = k
        else:
            del shark_loca[i]


    return time


def main():
    N, M, k = map(int, input().split())
    board = [[[] for _ in range(N)] for _ in range(N)]
    shark_loca = {}
    for i in range(N):
        board_row = list(map(int, input().split()))
        for j in range(N):
            if board_row[j] != 0:
                board[i][j] = [board_row[j], k]
                shark_loca[board[i][j][0]] = [i,j]
            else:
                board[i][j] = [board_row[j], 0]
    shark_dire = list(map(int, input().split()))
    shark_info = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
    shark_loca = dict(sorted(shark_loca.items()))
    time = 0

    while len(shark_loca) != 1:
        time = shark_move(N, M, k, board, shark_loca, shark_dire, shark_info, time)
        if time > 1000:
            time = -1
            break
    
    print(time)
    return time


if __name__ == '__main__':
    main()


# print(shark_loca, shark_dire)
# for i in range(M):
#     print(board[i])
# for i in range(M):
#  print(shark_info[i])