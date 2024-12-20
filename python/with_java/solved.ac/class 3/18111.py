import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
board = []
minH = 256
maxH = 0
for i in range(n):
    board.append(list(map(int, input().split())))
    minH = min(minH, min(board[i]))
    maxH = max(maxH, max(board[i]))
    b += sum(board[i])

maxH = min(maxH, b // (n * m))

minC = n * m * 2 * 256
resultH = 0
for h in range(minH, maxH+1):
    cost = 0
    for i in range(n):
        for j in range(m):
            temp = h - board[i][j]
            cost += temp if temp >= 0 else -2 * temp
    if minC < cost:
        break
    minC = cost
    resultH = h

print(minC, resultH)