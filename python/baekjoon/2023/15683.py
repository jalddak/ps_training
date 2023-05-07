first_row = list(map(int, input().split()))
n = first_row[0]
m = first_row[1]

cctvs = []

board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if 0 < board[i][j] < 6:
            cctvs.append([i, j])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = n * m

def check(bc, y, x, i):
    global dy, dx
    if i > 3:
        i -= 4
    ny = y + dy[i]
    nx = x + dx[i]
    while ny >= 0 and ny < n and nx >= 0 and nx < m and bc[ny][nx] != 6:
        if bc[ny][nx] == 0:
            bc[ny][nx] = 7
        ny += dy[i]
        nx += dx[i]

def dfs(board, cctvs):
    global n, m, dy, dx, result

    blind_num = 0
    if len(cctvs) == 0:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    blind_num += 1
        result = min(result, blind_num)
        return 0

    csc = cctvs[:]
    y, x = csc.pop()

    if board[y][x] == 1:
        for i in range(4):
            bc = [board[j][:] for j in range(n)]
            check(bc, y, x, i)
            dfs(bc, csc)

    elif board[y][x] == 2:
        for i in range(2):
            bc = [board[j][:] for j in range(n)]
            check(bc, y, x, i)
            check(bc, y, x, i+2)
            dfs(bc, csc)

    elif board[y][x] == 3:
        for i in range(4):
            bc = [board[j][:] for j in range(n)]
            check(bc, y, x, i)
            check(bc, y, x, i+1)
            dfs(bc, csc)

    elif board[y][x] == 4:
        for i in range(4):
            bc = [board[j][:] for j in range(n)]
            check(bc, y, x, i)
            check(bc, y, x, i+1)
            check(bc, y, x, i+2)
            dfs(bc, csc)

    elif board[y][x] == 5:
        bc = [board[j][:] for j in range(n)]
        check(bc, y, x, 0)
        check(bc, y, x, 1)
        check(bc, y, x, 2)
        check(bc, y, x, 3)
        dfs(bc, csc)

def main():
    global board, cctvs, result
    dfs(board, cctvs)
    print(result)

if __name__ == '__main__':
    main()