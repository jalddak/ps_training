T = int(input())

printStack = []
for t in range(1, T+1):
    rstr = "#" + str(t) + " "
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    stack = [(0, 0, 0)]
    visited[0][0] = True
    result = 0
    while len(stack) != 0:
        total, y, x = stack.pop()
        if (y, x) == (N-1, N-1):
            result = total
            break
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = True
                stack.append((total + board[ny][nx], ny, nx))
        stack.sort(key=lambda x:x[0], reverse=True)
    rstr += str(result)
    printStack.append(rstr)

for r in printStack:
    print(r)
