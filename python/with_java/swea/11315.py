tcCnt = int(input())

dy = [1, 0, 1, 1]
dx = [-1, 1, 1, 0]

answer = []
for tc in range(1, tcCnt + 1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    result = "NO"
    visited = [[[False for _ in range(n)] for _ in range(n)] for _ in range(4)]

    flag = False
    for d in range(4):
        for i in range(n):
            for j in range(n):
                if board[i][j] == "." or visited[d][i][j]:
                    continue
                visited[d][i][j] = True
                stack = [(i, j)]
                cnt = 0
                while stack:
                    cnt += 1
                    if cnt >= 5:
                        flag = True
                        result = "YES"
                        break
                    y, x = stack.pop()
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny >= n or ny < 0 or nx >= n or nx < 0 or board[ny][nx] == "." or visited[d][ny][nx]:
                        continue
                    visited[d][ny][nx] = True
                    stack.append((ny, nx))
                if flag:
                    break
            if flag:
                break
        if flag:
            break


    sb = "#" + str(tc) + " " + result
    answer.append(sb)

print("\n".join(answer))