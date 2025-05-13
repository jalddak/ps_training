tcCnt = 10

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = []
for _ in range(tcCnt):
    tc = int(input())
    sb = "#" + str(tc) + " "
    board = [list(map(int, list(input()))) for _ in range(100)]

    start = []
    end = []
    for i in range(100):
        for j in range(100):
            if board[i][j] == 2:
                start = [i, j]
                continue
            if board[i][j] == 3:
                end = [i, j]
                continue
    
    visited = [[False for _ in range(100)] for _ in range(100)]
    stack = [start]
    visited[start[0]][start[1]] = True
    result = 0
    while stack:
        y, x = stack.pop()
        if y == end[0] and x == end[1]:
            result = 1
            break

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny >= 100 or ny < 0 or nx >= 100 or nx < 0 or visited[ny][nx] or board[ny][nx] == 1:
                continue
            visited[ny][nx] = True
            stack.append([ny, nx])
    
    sb += str(result)
    answer.append(sb)


for a in answer:
    print(a)