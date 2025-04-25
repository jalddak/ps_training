answer = []

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for _ in range(1, 11):
    tc = int(input())
    sb = "#" + str(tc) + " "

    board = [list(map(int, list(input()))) for _ in range(16)]

    sy, sx = 0, 0
    ey, ex = 0, 0
    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                sy, sx = i, j
            if board[i][j] == 3:
                ey, ex = i, j
    
    stack = [(sy, sx)]
    visited = [[False for _ in range(16)] for _ in range(16)]
    visited[sy][sx] = True
    result = 0

    while stack:
        y, x = stack.pop()
        if (y, x) == (ey, ex):
            result = 1
            break
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= 16 or nx < 0 or nx >= 16 or visited[ny][nx] or board[ny][nx] == 1:
                continue
            stack.append((ny, nx))
            visited[ny][nx] = True
    
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)
