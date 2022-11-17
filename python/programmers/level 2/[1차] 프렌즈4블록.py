dy = [0, 0, 1, 1]
dx = [0, 1, 1, 0]

def solution(m, n, board):
    answer = 0
    removes = []
    for i in range(m):
        board[i] = list(board[i])
    while True:
        for i in range(m-1):
            for j in range(n-1):
                block = board[i][j]
                
                if block != '0'and\
                block == board[i + dy[1]][j + dx[1]] and\
                block == board[i + dy[2]][j + dx[2]] and\
                block == board[i + dy[3]][j + dx[3]]:
                    remove = []
                    for k in range(4):
                        my = i + dy[k]
                        mx = j + dx[k]
                        if (my, mx) not in removes:
                            remove.append((my, mx))
                    removes += remove
        if len(removes) == 0:
            break
        else:
            for remove in removes:
                answer += 1
                y = remove[0]
                x = remove[1]
                board[y][x] = '0'
                for i in range(y, 0, -1):
                    copy = board[i-1][x]
                    board[i-1][x] = board[i][x]
                    board[i][x] = copy
        removes = []
    return answer