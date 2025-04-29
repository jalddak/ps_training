# import sys
# sys.stdin = open('./python/with_java/swea/input.txt', 'r')
# sys.stdout = open('./python/with_java/swea/output.txt', 'w')

tcCnt = int(input())

answer = []

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(1, tcCnt + 1):
    sb = "#" + str(tc) + " "
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = [[0 for _ in range(n)] for _ in range(n)]

    result = [0, 0]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                stack = [(i, j)]
                cnt = 0
                while stack:
                    cnt += 1
                    y, x = stack.pop()
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] != board[y][x] + 1:
                            continue
                        if visited[ny][nx]:
                            cnt += count[ny][nx]
                            break
                        visited[ny][nx] = True
                        stack.append((ny, nx))
                count[i][j] = cnt
                if cnt >= result[1]:
                    if cnt > result[1] or result[0] > board[i][j] or result[0] == 0:
                        result[0] = board[i][j]
                    result[1] = cnt
    
    sb += str(result[0]) + " " + str(result[1])
    answer.append(sb)

for a in answer:
    print(a)