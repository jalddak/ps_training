import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()[:-1]) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if board[i][j] != 'I':
            continue
        visited[i][j] = True
        stack = [(i, j)]
        while(stack):
            y, x = stack.pop()
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if not (0 <= ny < n and 0 <= nx < m) or visited[ny][nx] or board[ny][nx] == "X":
                    continue
                stack.append((ny, nx))
                visited[ny][nx] = True
                if board[ny][nx] == "P":
                    answer += 1
        
if answer == 0:
    print("TT")
else:
    print(answer)