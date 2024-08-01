def solution(m, n, puddles):
    answer = 0
    board = [[0 for _ in range(m+1)] for _ in range(n+1)]
    board[1][1] = 1
    puddles = set(map(tuple, puddles))
    for y in range(1, n+1):
        for x in range(1, m+1):
            if y == 1 and x == 1:
                continue
            if (x, y) in puddles:
                board[y][x] = 0
                continue
            board[y][x] = (board[y-1][x] + board[y][x-1]) % 1000000007
            
    answer = board[n][m]
    return answer