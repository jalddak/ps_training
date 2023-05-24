r, c, t = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(r)]

def spread(board):
    global r, c
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    change = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                # spread amount
                sa = board[i][j] // 5
                cnt = 0
                for k in range(4):
                    sy = i + dy[k]
                    sx = j + dx[k]
                    if 0 <= sy < r and 0 <= sx < c and board[sy][sx] != -1:
                        change[sy][sx] += sa
                        cnt += 1
                change[i][j] -= (sa * cnt)
    for i in range(r):
        for j in range(c):
            board[i][j] += change[i][j]

def clean(board, cleaner):
    global r, c
    up = cleaner[0]
    down = cleaner[1]
    copy = []
    for i in range(r):
        copy.append(board[i][:])

    board[up][1] = 0
    for i in range(1, c-1):
        board[up][i+1] = copy[up][i]
    for i in range(up, 0, -1):
        board[i-1][c-1] = copy[i][c-1]
    for i in range(c-1, 0, -1):
        board[0][i-1] = copy[0][i]
    for i in range(up-1):
        board[i+1][0] = copy[i][0]

    board[down][1] = 0
    for i in range(1, c-1):
        board[down][i+1] = copy[down][i]
    for i in range(down, r-1):
        board[i+1][c-1] = copy[i][c-1]
    for i in range(c-1, 0, -1):
        board[r-1][i-1] = copy[r-1][i]
    for i in range(r-1, down+1, -1):
        board[i-1][0] = copy[i][0]

def main():
    global r, c, t, board
    cleaner = []
    for i in range(r):
        if board[i][0] == -1:
            cleaner.append(i)
    
    for i in range(t):
        spread(board)
        clean(board, cleaner)

    result = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                result += board[i][j]
    print(result)

if __name__ == '__main__':
    main()
