# BFS

from collections import deque
from itertools import combinations

N, M, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

candidateNums = [i for i in range(M)]
candidateNums = list(combinations(candidateNums, 3))

dy = [0, -1, 0]
dx = [-1, 0, 1]

result = 0
for cols in candidateNums:
    copy = []
    for i in range(N):
        copy.append(board[i][:])
    r = N
    temp = 0
    while r >= 0:
        die = []
        for c in cols:
            queue = deque([[r, c, 0]])
            check = 0
            visited = [[0 for _ in range(M)] for _ in range(N)]
            while len(queue) != 0 and check == 0:
                y, x, depth = queue.popleft()
                if depth == D:
                    continue
                for d in range(3):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < r and 0 <= nx < M and visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        if copy[ny][nx] != 1:
                            queue.append([ny, nx, depth + 1])
                        elif copy[ny][nx] == 1:
                            die.append((ny, nx))
                            check = 1
                            break
        die = set(die)
        temp += len(die)
        for ny, nx in list(die):
            copy[ny][nx] = 0
        r -= 1
        die
    result = max(result, temp)

print(result)