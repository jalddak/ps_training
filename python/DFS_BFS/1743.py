# DFS

N, M, K = list(map(int, input().split()))
board = [['.' for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c = list(map(lambda x:x-1, list(map(int, input().split()))))
    board[r][c] = '#'

dy = [-1, 0, 1 ,0]
dx = [0, 1, 0, -1]

result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '#' and not visited[i][j]:
            visited[i][j] = True
            stack = [[i, j]]
            cnt = 0
            while len(stack) != 0:
                cnt += 1
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == '#' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        stack.append([ny, nx])
            result = max(result, cnt)

print(result)