R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

dy = [-1, 0, 1]
dx = [1, 1, 1]

def main():
    result = 0
    for i in range(R):
        board[i][0] = 'X'
        check = dfs(i, 0)
        if check:
            result += 1
    print(result)

def dfs(y, x):
    global board
    if x == C-1:
        return True
    check = False
    for d in range(3):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == '.' and not check:
            check = dfs(ny, nx)
    board[y][x] = 'X'
    return check
            

if __name__ == '__main__':
    main()