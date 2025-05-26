import sys
def input():
    return sys.stdin.readline().strip()

def bfs():
    k = int(input())

    w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]

    visited = [[[False for _ in range(w)] for _ in range(h)] for _ in range(k + 1)]
    for i in range(k + 1):
        visited[i][0][0] = True

    from collections import deque
    q = deque([(k, 0, 0, 0)])

    hy = [-1, -2, -2, -1, 1, 2, 2, 1]
    hx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    def check(y, x, cnt, q, depth):
        if y >= h or y < 0 or x >= w or x < 0 or board[y][x] == 1 or visited[cnt][y][x]:
            return
        for i in range(cnt + 1):
            visited[i][y][x] = True
        q.append((cnt, y, x, depth + 1))


    result = -1
    while q:
        cnt, y, x, depth = q.popleft()
        if y == h-1 and x == w-1:
            result = depth
            break
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            check(ny, nx, cnt, q, depth)

        if cnt == 0:
            continue
        for d in range(8):
            ny = y + hy[d]
            nx = x + hx[d]
            check(ny, nx, cnt - 1, q, depth)

    print(result)

if __name__ == "__main__":
    bfs()