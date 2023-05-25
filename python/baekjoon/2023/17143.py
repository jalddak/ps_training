r, c, m = list(map(int, input().split()))
board = [[[] for _ in range(c)] for _ in range(r)]
# (y, x)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
# shark_location
sl = []
for _ in range(m):
    y, x, s, d, z = list(map(int, input().split()))
    sl.append((y-1, x-1))
    board[y-1][x-1] = [s, d, z]

result = 0

def catch_shark(board, man):
    global r, c, m, result, sl

    for i in range(r):
        if len(board[i][man]) != 0:
            result += board[i][man][2]
            sl.remove((i, man))
            board[i][man] = []
            m -= 1
            break

def move_shark(board):
    global r, c, m, sl
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, 1, -1]

    next = [[[] for _ in range(c)] for _ in range(r)]
    delete = []
    for i in range(m):
        y, x = sl[i]
        s, d, z = board[y][x]
        for _ in range(s):
            if y + dy[d] >= r or x + dx[d] < 0:
                d -= 1
            elif y + dy[d] < 0 or x + dx[d] >= c:
                d += 1
            y += dy[d]
            x += dx[d]
        if len(next[y][x]) == 0:
            next[y][x] = [s, d, z]
            sl.append((y, x))
        elif next[y][x][2] < z:
            next[y][x] = [s, d, z]
    sl = sl[m:]
    m = len(sl)
    return next
    

def main():
    global r, c, m, board, result, sl

    for i in range(c):
        catch_shark(board, i)
        board = move_shark(board)

    print(result)

if __name__ == '__main__':
    main()
