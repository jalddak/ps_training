def solution(board):
    answer = 0
    x = [-1, 0, 1, 1, 1, 0, -1, -1]
    y = [-1, -1, -1, 0, 1, 1, 1, 0]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    dangerY = i + y[k]
                    dangerX = j + x[k]
                    if dangerY >= 0 and dangerY < n and dangerX >= 0 and dangerX < n:
                        if board[dangerY][dangerX] != 1:
                            board[dangerY][dangerX] = 2
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    return answer