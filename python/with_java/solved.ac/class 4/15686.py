n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))
        
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 1e9


def calcDistance(cy, cx, distances):
    result = [0 for _ in range(len(homes))]
    for i in range(len(homes)):
        hy, hx = homes[i]
        result[i] = min(distances[i], abs(hy-cy) + abs(hx-cx))
    return result


def solution(depth, distances, k):
    global answer
    if depth == m:
        answer = min(sum(distances), answer)
        return

    for i in range(k, len(chickens) - m + depth + 1):
        cy, cx = chickens[i]
        nDistances = calcDistance(cy, cx, distances)
        solution(depth + 1, nDistances, i+1)

solution(0, [1e9 for _ in range(len(homes))], 0)
print(answer)