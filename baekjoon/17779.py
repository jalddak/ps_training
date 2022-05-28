def divide_board(N, x, y, d1, d2):
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(d1+1):
        for j in range(d2+1):
            board[x+i+j][y-i+j] = 5
    for i in range(x+d1):
        for j in range(y+1):
            if board[i][j] == 5:
                break
            board[i][j] = 1
    for j in range(y+1, N):
        for i in range(x+d2+1):
            if board[i][j] == 5:
                break
            board[i][j] = 2
    for i in range(x+d1, N):
        for j in range(y-d1+d2):
            if board[i][j] == 5:
                break
            board[i][j] = 3
    for j in range(y-d1+d2, N):
        for i in range(N-1, x+d2, -1):
            if board[i][j] == 5:
                break
            board[i][j] = 4
    return board


def check_min(N, board, divided, result):
    one = 0
    two = 0
    three = 0 
    four = 0
    five = 0
    for i in range(N):
        for j in range(N):
            if divided[i][j] == 1:
                one += board[i][j]
            elif divided[i][j] == 2:
                two += board[i][j]
            elif divided[i][j] == 3:
                three += board[i][j]
            elif divided[i][j] == 4:
                four += board[i][j]
            elif divided[i][j] == 0 or  divided[i][j] == 5:
                five += board[i][j]
    max_population = max(one,two,three,four,five)
    min_population = min(one,two,three,four,five)
    result = min(result, max_population - min_population)
    return result

def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # x = 행(가로줄) y = 열(세로줄) 이다.
    result = N*N*100
    for x in range(N-2):
        for y in range(1, N-1):
            for d1 in range(1, N-1):
                for d2 in range(1, N-1):
                    if x+d1+d2 > N-1 or y-d1 < 0 or y+d2 > N-1:
                        continue
                    divided = divide_board(N, x, y, d1, d2)
                    result = check_min(N, board, divided, result)
    print(result)
    return result

if __name__ == '__main__':
    main()