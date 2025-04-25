n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    checked = [[0 for _ in range(m)] for _ in range(n)]

    visited[0][0] = True
    stack = [(0, 0)]
    candidates = []

    while stack:
        y, x = stack.pop()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny >= n or ny < 0 or nx >= m or nx < 0 or visited[ny][nx]:
                continue
            if board[ny][nx] == 1:
                checked[ny][nx] += 1
                if checked[ny][nx] == 2:
                    candidates.append((ny, nx))
                continue
            stack.append((ny, nx))
            visited[ny][nx] = True
    
    if candidates:
        answer += 1
    else:
        print(answer)
        break

    while candidates:
        y, x = candidates.pop()
        board[y][x] = 0