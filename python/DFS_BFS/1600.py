from collections import deque

K = int(input())

W, H = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[-1 for _ in range(W)] for _ in range(H)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

hy = [-2, -1, 1, 2, 2, 1, -1, -2]
hx = [1, 2, 2, 1, -1, -2, -2, -1]

queue = deque([])
y, x = (0, 0)
cnt = 0
visited[y][x] = K
queue.append([y, x, K, cnt])

while len(queue) != 0:
    y, x, k, cnt = queue.popleft()
    if (y, x) == (H-1, W-1):
        print(cnt)
        exit()
    
    ncnt = cnt + 1
    if k > 0:
        nk = k - 1
        for h in range(8):
            ny = y + hy[h]
            nx = x + hx[h]
            if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == 0 and nk > visited[ny][nx]:
                visited[ny][nx] = nk
                queue.append([ny, nx, nk, ncnt])
    
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == 0 and k > visited[ny][nx]:
            visited[ny][nx] = k
            queue.append([ny, nx, k, ncnt])
    
print(-1)