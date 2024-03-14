def solution(board):
    n, m = len(board), len(board[0])
    dy = [0, -1, -1]
    dx = [-1, -1, 0]
    
    max_len = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            check = True
            min_n = 1001
            for d in range(3):
                ay = i + dy[d]
                ax = j + dx[d]
                if 0<=ay<n and 0<=ax<m and board[ay][ax] >= 1:
                    min_n = min(min_n, board[ay][ax])
                    continue
                check = False
                break
            if check:
                board[i][j] = min_n + 1
            max_len = max(max_len, board[i][j])
    
    return max_len * max_len