# x = row, y = col 이다.

def check_blue(board, score):
    i = 9
    while i > 5:
        for j in range(4):
            if board[j][i] != 1:
                break
            elif j == 3:
                score += 1
                for k in range(4):
                    board[k].pop(i)
                    board[k].insert(0, 0)
                i += 1
        i -= 1

    pop_count = 0
    while i > 3:
        for j in range(4):
            if board[j][i] == 1:
                pop_count += 1
                break
        i -= 1

    for _ in range(pop_count):
        for j in range(4):
            board[j].pop()
            board[j].insert(0, 0)
        
    return score


def check_green(board, score):
    i = 9
    while i > 5:
        if sum(board[i]) == 4:
            score += 1
            board.pop(i)
            board.insert(4, [0,0,0,0,0,0,0,0,0,0])
            i += 1
        i -= 1

    pop_count = 0
    while i > 3:
        if sum(board[i]) > 0:
            pop_count += 1
        i -= 1

    for _ in range(pop_count):
        board.pop()
        board.insert(4, [0,0,0,0,0,0,0,0,0,0])
    return score


def main():
    board = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    score = 0
    for _ in range(N):
        t, x, y = map(int, input().split())
        if t == 1:
            # 파랑
            for i in range(6, 10):
                if board[x][i] == 1:
                    board[x][i-1] = 1
                    break 
                if i == 9:
                    board[x][i] = 1
            # 초록
            for i in range(6, 10):
                if board[i][y] == 1:
                    board[i-1][y] = 1
                    break
                if i == 9:
                    board[i][y] = 1
        elif t == 2:
            # 파랑
            for i in range(6, 10):
                if board[x][i] == 1:
                    board[x][i-1] = 1
                    board[x][i-2] = 1
                    break 
                if i == 9:
                    board[x][i] = 1
                    board[x][i-1] = 1
            # 초록
            for i in range(6, 10):
                if board[i][y] == 1 or board[i][y+1] == 1:
                    board[i-1][y] = 1
                    board[i-1][y+1] = 1
                    break
                if i == 9:
                    board[i][y] = 1
                    board[i][y+1] = 1
        elif t == 3:
            # 파랑
            for i in range(6, 10):
                if board[x][i] == 1 or board[x+1][i] == 1:
                    board[x][i-1] = 1
                    board[x+1][i-1] = 1
                    break
                if i == 9:
                    board[x][i] = 1
                    board[x+1][i] = 1
            # 초록
            for i in range(6, 10):
                if board[i][y] == 1:
                    board[i-1][y] = 1
                    board[i-2][y] = 1
                    break
                if i == 9:
                    board[i][y] = 1
                    board[i-1][y] = 1

        score = check_blue(board, score)
        score = check_green(board, score)

    count = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                count += 1
    print(score)
    print(count)
    return 0


if __name__ == '__main__':
    main()