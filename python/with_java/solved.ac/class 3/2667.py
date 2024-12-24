n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

cnts = []
dy = [-1 ,0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if board[i][j] == 0 or visited[i][j]:
            continue
        visited[i][j] = True
        s = [(i, j)]
        cnt = 0
        while s:
            y, x = s.pop()
            cnt += 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 1 and not visited[ny][nx]:
                    s.append((ny, nx))
                    visited[ny][nx] = True
        cnts.append(cnt)

cnts.sort()
print(len(cnts))
for cnt in cnts:
    print(cnt)