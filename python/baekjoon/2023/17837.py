from collections import deque

n, k = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
stack = [[[] for _ in range(n)] for _ in range(n)]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

hs = deque([])
for i in range(k):
    y, x, d = list(map(int, input().split()))
    y -= 1
    x -= 1
    d -= 1
    stack[y][x].append(i)
    hs.append([y, x, d])

def main():
    global n, k, board, stack, dy, dx, hs
    turn = 1

    while turn <= 1000:
        for i in range(k):
            y, x, d = hs[i]
            ny = y + dy[d]
            nx = x + dx[d]
            loca = stack[y][x].index(i)
            move_hs = stack[y][x][loca:]
            stack[y][x] = stack[y][x][:loca]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 2:
                if board[ny][nx] == 1:
                    move_hs.reverse()
            else:
                if d % 2 == 0:
                    d += 1
                else:
                    d -= 1
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 2:
                    if board[ny][nx] == 1:
                        move_hs.reverse()
                else:
                    ny = y
                    nx = x
            stack[ny][nx] += move_hs
            if len(stack[ny][nx]) >= 4:
                print(turn)
                return 0
            for num in move_hs:
                hs[num] = [ny, nx, hs[num][2]]
            hs[i] = [ny, nx, d]
        turn += 1
    print(-1)

if __name__ == '__main__':
    main()
