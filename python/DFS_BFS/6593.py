import sys
input = sys.stdin.readline

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

from collections import deque

result = []
while True:
    L, R, C = map(int, input().split())
    if L == 0:
        break
    
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]

    b = []
    for _ in range(L):
        floor = [list(input())[:-1] for _ in range(R)]
        b.append(floor)
        input()
    
    queue = deque([])
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if b[z][y][x] == "S":
                    queue.append([0, z, y, x])
                    visited[z][y][x] = True
                    break
    
    check = False
    while queue:
        cnt, z, y, x = queue.popleft()
        if b[z][y][x] == "E":
            result.append(cnt)
            check = True
            break
        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C and not visited[nz][ny][nx] and b[nz][ny][nx] != "#":
                queue.append([cnt+1, nz, ny, nx])
                visited[nz][ny][nx] = True
    
    if not check:
        result.append(0)

for r in result:
    if r == 0:
        print("Trapped!")
    else:
        print("Escaped in " + str(r) + " minute(s).")