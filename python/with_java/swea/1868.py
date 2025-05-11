tcCnt = int(input())

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

def checkAround(board, visited, y, x, stack):
    cnt = 0
    for d in range(8):
        ay = y + dy[d]
        ax = x + dx[d]
        if ay >= n or ay < 0 or ax >= n or ax < 0 or visited[ay][ax]:
            continue
        if board[ay][ax] == "*":
            cnt += 1
            continue
        stack.append((ay, ax))

    return cnt

answer = []
for tc in range(1, tcCnt + 1):
    sb = "#" + str(tc) + " "
    n = int(input())
    board = [list(input()) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    result = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] or board[i][j] == "*":
                continue

            temp = []
            cnt = checkAround(board, visited, i, j, temp)
            if cnt != 0:
                continue
            
            result += 1
            visited[i][j] = True
            
            stack = []
            for y, x in temp:
                visited[y][x] = True
                stack.append((y, x))

            while stack:
                y, x = stack.pop()
                temp = []
                cnt = checkAround(board, visited, y, x, temp)
                if cnt != 0:
                    continue

                for ty, tx in temp:
                    visited[ty][tx] = True
                    stack.append((ty, tx))

    for i in range(n):
        for j in range(n):
            if visited[i][j] or board[i][j] == "*":
                continue
            result += 1

    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)