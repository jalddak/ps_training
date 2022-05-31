from collections import deque

def dfs(board, horse_list, distance_list, now_score, best_score):
    check_horse = set(horse_list)
    distance_save = distance_list.popleft()
    horse_list_copy = horse_list[:]
    now_score_copy = now_score

    for i in range(len(check_horse)):
        distance = distance_save
        distance_list_copy = deque(list(distance_list)[:])
        if horse_list_copy[i][1] == 21:
            continue
        if horse_list_copy[i][1] == 5:
            if len(board[1]) < distance:
                distance -= len(board[1])
                if len(board[4]) < distance:
                    distance -= len(board[4])
                    if 20 + distance - 1 > 21:
                        horse_list_copy[i] = (0, 21)
                    else:
                        horse_list_copy[i] = (0, 20 + distance - 1)
                else:
                    horse_list_copy[i] = (4, distance - 1)
            else:
                horse_list_copy[i] = (1, distance - 1)

        elif horse_list_copy[i][1] == 10:
            if len(board[2]) < distance:
                distance -= len(board[2])
                if len(board[4]) < distance:
                    distance -= len(board[4])
                    if 20 + distance - 1 > 21:
                        horse_list_copy[i] = (0, 21)
                    else:
                        horse_list_copy[i] = (0, 20 + distance - 1)
                else:
                    horse_list_copy[i] = (4, distance - 1)
            else:
                horse_list_copy[i] = (2, distance - 1)

        elif horse_list_copy[i][1] == 15:
            if len(board[3]) < distance:
                distance -= len(board[3])
                if len(board[4]) < distance:
                    distance -= len(board[4])
                    if 20 + distance - 1 > 21:
                        horse_list_copy[i] = (0, 21)
                    else:
                        horse_list_copy[i] = (0, 20 + distance - 1)
                else:
                    horse_list_copy[i] = (4, distance - 1)
            else:
                horse_list_copy[i] = (3, distance - 1)

        elif len(board[horse_list_copy[i][0]]) < distance + horse_list_copy[i][1] + 1:
            if horse_list_copy[i][0] == 0:
                horse_list_copy[i] = (0, 21)
            elif horse_list_copy[i][0] == 1:
                distance -= (len(board[1]) - (horse_list_copy[i][1] + 1))
                if len(board[4]) < distance:
                    distance -= len(board[4])
                    if 20 + distance - 1 > 21:
                        horse_list_copy[i] = (0, 21)
                    else:
                        horse_list_copy[i] = (0, 20 + distance - 1)
                else:
                    horse_list_copy[i] = (4, distance - 1)
            elif horse_list_copy[i][0] == 2:
                distance -= (len(board[2]) - (horse_list_copy[i][1] + 1))
                if len(board[4]) < distance:
                    distance -= len(board[4])
                    if 20 + distance - 1 > 21:
                        horse_list_copy[i] = (0, 21)
                    else:
                        horse_list_copy[i] = (0, 20 + distance - 1)
                else:
                    horse_list_copy[i] = (4, distance - 1)
                
            elif horse_list_copy[i][0] == 3:
                distance -= (len(board[3]) - (horse_list_copy[i][1] + 1))
                if len(board[4]) < distance:
                    distance -= len(board[4])
                    if 20 + distance - 1 > 21:
                        horse_list_copy[i] = (0, 21)
                    else:
                        horse_list_copy[i] = (0, 20 + distance - 1)
                else:
                    horse_list_copy[i] = (4, distance - 1)

            elif horse_list_copy[i][0] == 4:
                distance -= (len(board[4]) - (horse_list_copy[i][1] + 1))
                if 20 + distance - 1 > 21:
                    horse_list_copy[i] = (0, 21)
                else:
                    horse_list_copy[i] = (0, 20 + distance - 1)

        else:
            horse_list_copy[i] = (horse_list_copy[i][0], horse_list_copy[i][1] + distance)

        if horse_list_copy[i] not in horse_list:
            if horse_list_copy[i] == (0,21):
                horse_list_copy.pop(i)
            else:
                now_score += board[horse_list_copy[i][0]][horse_list_copy[i][1]]
            if len(distance_list) > 0:
                best_score = dfs(board, horse_list_copy, distance_list_copy, now_score, best_score)
            else:
                best_score = max(best_score, now_score)
        horse_list_copy = horse_list[:]
        now_score = now_score_copy
    
    return best_score


def main():
    board = [[i*2 for i in range(22)]]
    board[0][len(board[0])-1] = 0
    board.append([13, 16, 19])
    board.append([22, 24])
    board.append([28, 27, 26])
    board.append([25, 30, 35])

    horse_list = [(0,0) for _ in range(4)]
    distance_list = deque(list(map(int, input().split())))

    best_score = dfs(board, horse_list, distance_list, 0, 0)
    print(best_score)
    return best_score


if __name__ =='__main__':
    main()