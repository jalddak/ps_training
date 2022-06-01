# x = row, y = col 이다.

def check_blue(board, score):
    for i in range(9, 5, -1):
        for j in range(4):
            if board[j][i] != 1:
                break
            elif j == 3:
                score += 1
                

def main():
    board = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    score = 0
    for _ in range(N):
        t, x, y = map(int, input().split())
        if t == 1:
            # 파랑
            for i in range(9, 3, -1):
                if board[x][i] == 0:
                    board[x][i] = 1
                    break 
            # 초록
            for i in range(9, 3, -1):
                if board[i][y] == 0:
                    board[i][y] = 1
                    break 
        elif t == 2:
            # 파랑
            for i in range(9, 3, -1):
                if board[x][i] == 0 and board[x][i-1] == 0:
                    board[x][i] = 1
                    board[x][i-1] = 1
                    break 
            # 초록
            for i in range(9, 3, -1):
                if board[i][y] == 0 and board[i][y+1] == 0:
                    board[i][y] = 1
                    board[i][y+1] = 1
                    break
        elif t == 3:
            # 파랑
            for i in range(9, 3, -1):
                if board[x][i] == 0 and board[x+1][i] == 0:
                    board[x][i] = 1
                    board[x+1][i] = 1
                    break 
            # 초록
            for i in range(9, 3, -1):
                if board[i][y] == 0 and board[i-1][y] == 0:
                    board[i][y] = 1
                    board[i-1][y] = 1
                    break 
        


if __name__ == '__main__':
    main()