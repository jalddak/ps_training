(시간초과)

import sys
input = sys.stdin.readline
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
f_locas = [tuple(map(lambda x:x-1, map(int, input().split()))) for _ in range(m)]

candidates = [[] for _ in range(m)]
def dfs(y, x, result, visited, index):
    global m
    if len(result) == 4:
        candidates[index].append(set(result))
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            result.append((ny, nx))
            visited[ny][nx] = True
            dfs(ny, nx, result, visited, index)
            visited[ny][nx] = False
            result.pop()
            
for i in range(m):
    y, x = f_locas[i]
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[y][x] = True
    dfs(y, x, [(y, x)], visited, i)

answer = 0
def select(depth, result):
    global m, candidates, board, answer
    if depth == m:
        selected = set()
        for i in range(m):
            selected = selected | candidates[i][result[i]]
        selected = list(selected)
        result = 0
        for y, x in selected:
            result += board[y][x]
            answer = max(result, answer)
        return
    for i in range(len(candidates[depth])):
        result.append(i)
        select(depth+1, result)
        result.pop()

select(0, [])
print(answer)