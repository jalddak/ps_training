import sys
sys.setrecursionlimit(10**6)

n, m, p = map(int, input().split())
s = [0] + list(map(int, input().split()))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

board = [list(input()) for _ in range(n)]

stacks = [[] for _ in range(p+1)]
answer = [0 for _ in range(p+1)]

for i in range(n):
    for j in range(m):
        if board[i][j].isdigit():
            stacks[int(board[i][j])].append((i, j))
            answer[int(board[i][j])] += 1

flag = True

def recursion(stack, depth, num):
    next = []
    while stack:
        y, x = stack.pop()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny >= n or ny < 0 or nx >= m or nx < 0 or board[ny][nx] != ".":
                continue
            board[ny][nx] = str(num)
            answer[num] += 1
            next.append((ny, nx))
    if depth + 1 < s[num] and next:
        next = recursion(next, depth + 1, num)
    return next

while flag:
    flag = False
    for i in range(1, p+1):
        stack = stacks[i]
        next = recursion(stack, 0, i)
        if next:
            stacks[i] = next
            flag = True

print(" ".join(map(str, answer[1:])))