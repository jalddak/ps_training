N, M, K = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]

dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
d = 0


def roll(dice, d):
    # 동 남 서 북 순서
    temp = dice[3][1]
    if d == 0:
        dice[3][1] = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = temp
    elif d == 1:
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = temp
    elif d == 2:
        dice[3][1] = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = temp
    elif d == 3:
        dice[3][1] = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = temp


def check(board, y, x):
    global N, M, dy, dx

    visited = [[0 for _ in range(M)] for _ in range(N)]
    num = board[y][x]
    visited[y][x] = 1
    stack = [[y, x]]
    cnt = 1
    while len(stack) != 0:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == num and visited[ny][nx] == 0:
                cnt += 1
                visited[ny][nx] = 1
                stack.append([ny, nx])

    return num * cnt


def main():
    global N, M, K, board, dice, dy, dx, d

    y, x = [0, 0]
    score = 0
    for _ in range(K):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            d += 2
            if d >= 4:
                d -= 4
            ny = y + dy[d]
            nx = x + dx[d]
        roll(dice, d)
        score += check(board, ny, nx)
        if dice[3][1] > board[ny][nx]:
            d += 1
            if d == 4:
                d -= 4
        elif dice[3][1] < board[ny][nx]:
            d -= 1
            if d == -1:
                d += 4
        y, x = [ny, nx]
    print(score)


if __name__ == '__main__':
    main()