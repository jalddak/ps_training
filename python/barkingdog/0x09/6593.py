from collections import deque

answer = []

dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 0, 1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    building = []
    q = deque()
    end = []
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]
    for i in range(l):
        building.append([])
        for j in range(r):
            building[i].append(list(input()))
            for k in range(c):
                if building[i][j][k] == "S":
                    visited[i][j][k] = True
                    q.append((i, j, k, 0))
        input()

    result = -1
    while q:
        z, y, x, time = q.popleft()
        if building[z][y][x] == "E":
            result = time
            break
        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]
            if nz >= l or nz < 0 or ny >= r or ny < 0 or nx >= c or nx < 0 or building[nz][ny][nx] == "#" or visited[nz][ny][nx]:
                continue
            visited[nz][ny][nx] = True
            q.append((nz, ny, nx, time + 1))


    if result == -1:
        answer.append("Trapped!")
    else:
        answer.append("Escaped in " + str(result) + " minute(s).")

print("\n".join(answer))