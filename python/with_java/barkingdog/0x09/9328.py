t = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

lower = set()
upper = set()
for i in range(26):
    a = ord('a')
    A = ord('A')
    lower.add(chr(i + a))
    upper.add(chr(i + A))

answer = []
for _ in range(t):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    stack = []
    for i in range(h):
        if board[i][0] != "*" and not visited[i][0]:
            visited[i][0] = True
            stack.append((i, 0))
        if board[i][w-1] != "*" and not visited[i][w-1]:
            visited[i][w-1] = True
            stack.append((i, w-1))
    
    for i in range(w):
        if board[0][i] != "*" and not visited[0][i]:
            visited[0][i] = True
            stack.append((0, i))
        if board[h-1][i] != "*" and not visited[h-1][i]:
            visited[h-1][i] = True
            stack.append((h-1, i))
    
    key = set()
    keyInput = list(input())
    if keyInput[0] != '0':
        key = set(keyInput)

    result = 0
    flag = True
    while flag:
        flag = False
        next = []
        while stack:
            y, x = stack.pop()
            if board[y][x] in upper and chr(ord(board[y][x]) + 32) not in key:
                next.append((y, x))
                continue
            if board[y][x] in lower:
                flag = True
                key.add(board[y][x])
            if board[y][x] == "$":
                result += 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if ny >= h or ny < 0 or nx >= w or nx < 0 or board[ny][nx] == "*" or visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                stack.append((ny, nx))
        stack = next
    answer.append(result)

print("\n".join(map(str, answer)))