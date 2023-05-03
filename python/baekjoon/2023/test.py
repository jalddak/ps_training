first = list(map(int, input().split()))

global n, m, y, x, k
n, m, y, x, k = first

global board, dy, dx, ds, dice
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

ds = list(map(int, input().split()))
# 동 서 북 남
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]

def move(d):
    global n, m, y, x, dice, dy, dx, board
    ny = y + dy[d]
    nx = x + dx[d]
    if ny > n-1 or ny < 0 or nx > m-1 or nx < 0:
        return 0
    y = ny
    x = nx

    d0, d1, d2, d3, d4, d5 = dice
    if d == 0:
        dice[0] = d5
        dice[1] = d3
        dice[3] = d0
        dice[5] = d1

    elif d == 1:
        dice[0] = d3
        dice[1] = d5
        dice[3] = d1
        dice[5] = d0

    elif d == 2:
        dice[0] = d4
        dice[1] = d2
        dice[2] = d0
        dice[4] = d1

    elif d == 3:
        dice[0] = d2
        dice[1] = d4
        dice[2] = d1
        dice[4] = d0

    if board[y][x] == 0:
        board[y][x] = dice[1]
    else:
        dice[1] = board[y][x]
        board[y][x] = 0

    print(dice[0])


def main():
    global k, ds
    for i in range(k):
        move(ds[i]-1)
    return 0

if __name__ == '__main__':
    main()