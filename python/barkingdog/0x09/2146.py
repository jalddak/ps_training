n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

from collections import deque
bfsList = []

check = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 0 or visited[i][j] != 0:
            continue
        check += 1
        board[i][j] = check
        visited[i][j] = check
        stack = [(i, j)]
        seaStack = deque()
        while stack:
            y, x = stack.pop()
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if ny >= n or ny < 0 or nx >= n or nx < 0 or visited[ny][nx] != 0:
                    continue
                visited[ny][nx] = check
                if board[ny][nx] == 0:
                    seaStack.append((ny, nx, 1, check))
                    continue
                board[ny][nx] = check
                stack.append((ny, nx))
        bfsList.append(seaStack)

result = n * n
for seaStack in bfsList:
    while seaStack:
        flag = False
        y, x, cnt, check = seaStack.popleft()
        if cnt >= result:
            break
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny >= n or ny < 0 or nx >= n or nx < 0 or visited[ny][nx] == check:
                continue
            if board[ny][nx] != 0:
                result = min(result, cnt)
                flag = True
                break
            visited[ny][nx] = check
            seaStack.append((ny, nx, cnt + 1, check))
        if flag:
            break

print(result)