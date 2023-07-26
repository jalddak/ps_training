# BFS

from collections import deque

N = int(input())
max_h = 0
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    max_h = max(max_h, max(row))
    board.append(row)

def bfs(height):
    global N, board
    visited = [[False for _ in range(N)] for _ in range(N)]

    area = 0
    queue = deque([])

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > height:
                visited[i][j] = True
                queue.append([i, j])
                area += 1
                while len(queue) != 0:
                    y, x = queue.popleft()
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and board[ny][nx] > height:
                            visited[ny][nx] = True
                            queue.append([ny, nx])
    return area


if __name__ == '__main__':
    max_area = 0
    for i in range(max_h):
        max_area = max(max_area, bfs(i))
    print(max_area)