r, c = map(int, input().split())

board = [list(input()) for _ in range(r)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0

# dfs 함수 활용 - 통과
def dfs(y, x, s):
    global answer
    answer = max(answer, len(s))
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < r and 0 <= nx < c and board[ny][nx] not in s:
            s.add(board[ny][nx])
            dfs(ny, nx, s)
            s.remove(board[ny][nx])

dfs(0, 0, set([board[0][0]]))
print(answer)

#bfs - 메모리 초과
from collections import deque
q = deque([(0, 0, set([board[0][0]]))])

while q:
    y, x, s = q.popleft()
    answer = max(answer, len(s))
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < r and 0 <= nx < c and board[ny][nx] not in s:
            ns = s | set([board[ny][nx]])
            q.append([ny, nx, ns])

print(answer)

#dfs - 시간 초과
stack = [(0, 0, set([board[0][0]]))]

while stack:
    y, x, s = stack.pop()
    answer = max(answer, len(s))
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < r and 0 <= nx < c and board[ny][nx] not in s:
            ns = s | set([board[ny][nx]])
            stack.append([ny, nx, ns])

print(answer)