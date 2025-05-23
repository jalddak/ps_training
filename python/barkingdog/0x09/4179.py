r, c = map(int, input().split())

board = [list(input()) for _ in range(r)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

human = []
fire = []

def spread(stack, flag):
    next = []
    result = False
    while stack:
        y, x = stack.pop()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny >= r or ny < 0 or nx >= c or nx < 0:
                if flag == "J":
                    result = True
                    return [], result
                continue
            if board[ny][nx] == "#" or board[ny][nx] == "F":
                continue
            if flag == "J" and board[ny][nx] == "J":
                continue
            board[ny][nx] = flag
            next.append((ny, nx))
    return next, result

for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            human.append((i, j))
        elif board[i][j] == "F":
            fire.append((i, j))

result = False
cnt = 0
while human:
    fire, reuslt = spread(fire, "F")
    human, result = spread(human, "J")
    cnt += 1

if result:
    print(cnt)
else:
    print("IMPOSSIBLE")