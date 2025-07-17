board = [list(input()) for _ in range(5)]
visited = [[False for _ in range(5)] for _ in range(5)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0

def check(y, x):
    checked = [[False for _ in range(5)] for _ in range(5)]
    checked[y][x] = True
    stack = [(y, x)]
    result = True
    cnt = 0
    sCnt = 0

    while stack:
        y, x = stack.pop()
        cnt += 1
        if board[y][x] == 'S':
            sCnt += 1
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny >= 5 or nx >= 5 or ny < 0 or nx < 0 or not visited[ny][nx] or checked[ny][nx]:
                continue
            checked[ny][nx] = True
            stack.append((ny, nx))
    
    if sCnt < 4 or cnt < 7:
        result = False
    return result

def recursion(depth, y, x):
    global answer
    if depth == 7:
        if check(y, x):
            answer += 1
        return

    for i in range(y, 5):
        for j in range(x, 5):
            if visited[i][j]:
                continue
            visited[i][j] = True
            recursion(depth + 1, i, j)
            visited[i][j] = False
        x = 0

recursion(0, 0, 0)

print(answer)