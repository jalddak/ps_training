#DFS

R, C = list(map(int, input().split()))

board = [[s for s in input()] for _ in range(R)]

# y, x, cnt, list
l = [False for _ in range(26)]
l[ord(board[0][0])-65] = True
stack = [[0, 0, 1, l]]

max_cnt = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while len(stack) != 0:
    y, x, cnt, l= stack.pop()
    if max_cnt < cnt:
        max_cnt = cnt
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < R and 0 <= nx < C:
            i = ord(board[ny][nx]) - 65
            if not l[i]:
                nl = l[:]
                nl[i] = True
                stack.append([ny, nx, cnt+1, nl])

print(max_cnt)