import sys
def input():
    return sys.stdin.readline().strip()

from collections import deque

tc = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(q, time, board, n, m, flag):
    while q and q[0][2] == time:
        y, x, t = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny >= n or ny < 0 or nx >= m or nx < 0:
                if flag == "@":
                    return True
                continue
            if board[ny][nx] == "#" or board[ny][nx] == "*":
                continue
            if flag == "@" and board[ny][nx] != ".":
                continue
            board[ny][nx] = flag
            q.append((ny, nx, t + 1))
    
    return False

answer = []
for _ in range(tc):
    m, n = map(int, input().split())
    board = [list(input()) for _ in range(n)]

    fire = deque()
    sang = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == "*":
                fire.append((i, j, 0))
            elif board[i][j] == "@":
                sang.append((i, j, 0))
    
    result = False
    time = 0
    while sang:
        bfs(fire, time, board, n, m, "*")
        result = bfs(sang, time, board, n, m, "@")
        time += 1
        if result:
            break
    if not result:
        time = "IMPOSSIBLE"
    answer.append(time)



print("\n".join(map(str, answer)))