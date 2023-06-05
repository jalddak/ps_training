N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def spread(board, d, y, x):
    global N, dy, dx

    out = 0
    left = d + 1
    right = d - 1
    front = d
    back = d + 2
    if left == 4:
        left = 0
    if right == -1:
        right = 3
    if back >= 4:
        back -= 4

    sand = board[y][x]

    f2 = 5*sand//100
    f1l1, f1r1 = 10*sand//100, 10*sand//100
    l1, r1 = 7*sand//100, 7*sand//100
    l2, r2 = 2*sand//100, 2*sand//100
    b1l1, b1r1 = sand//100, sand//100
    a = sand - (f2 + f1l1 + f1r1 + l1 + r1 + l2 + r2 + b1l1 + b1r1)

    if 0 <= y+2*dy[front] < N and 0 <= x+2*dx[front] < N:
        board[y+2*dy[front]][x+2*dx[front]] += f2
    else:
        out += f2

    if 0 <= y+dy[front] < N and 0 <= x+dx[front] < N:
        board[y+dy[front]][x+dx[front]] += a
    else:
        out += a

    if 0 <= y+dy[front]+dy[left] < N and 0 <= x+dx[front]+dx[left] < N:
        board[y+dy[front]+dy[left]][x+dx[front]+dx[left]] += f1l1
    else:
        out += f1l1
    
    if 0 <= y+dy[front]+dy[right] < N and 0 <= x+dx[front]+dx[right] < N:
        board[y+dy[front]+dy[right]][x+dx[front]+dx[right]] += f1r1
    else:
        out += f1r1
    
    if 0 <= y+dy[left] < N and 0 <= x+dx[left] < N:
        board[y+dy[left]][x+dx[left]] += l1
    else:
        out += l1
    
    if 0 <= y+dy[right] < N and 0 <= x+dx[right] < N:
        board[y+dy[right]][x+dx[right]] += r1
    else:
        out += r1
    
    if 0 <= y+2*dy[left] < N and 0 <= x+2*dx[left] < N:
        board[y+2*dy[left]][x+2*dx[left]] += l2
    else:
        out += l2
    
    if 0 <= y+2*dy[right] < N and 0 <= x+2*dx[right] < N:
        board[y+2*dy[right]][x+2*dx[right]] += r2
    else:
        out += r2

    if 0 <= y+dy[back]+dy[left] < N and 0 <= x+dx[back]+dx[left] < N:
        board[y+dy[back]+dy[left]][x+dx[back]+dx[left]] += b1l1
    else:
        out += b1l1
    
    if 0 <= y+dy[back]+dy[right] < N and 0 <= x+dx[back]+dx[right] < N:
        board[y+dy[back]+dy[right]][x+dx[back]+dx[right]] += b1r1
    else:
        out += b1r1

    board[y][x] = 0

    return out

def main():
    global N, board, dy, dx

    y, x = N // 2, N // 2
    d = 0
    cnt = 1
    s = 0
    result = 0
    while 0 <= y < N and 0 <= x < N:
        for _ in range(cnt):
            y += dy[d]
            x += dx[d]
            if 0 <= y < N and 0 <= x < N:
                result += spread(board, d, y, x)
        d += 1
        if d == 4:
            d = 0

        s += 1
        if s == 2:
            s = 0
            cnt += 1
    print(result)


if __name__ == '__main__':
    main()