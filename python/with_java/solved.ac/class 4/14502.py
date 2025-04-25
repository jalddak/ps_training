n, m = map(int, input().split())

board = []
virus = []
clean = []

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 0:
            clean.append([i, j])
        elif board[i][j] == 2:
            virus.append([i, j])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0

def check():
    global answer

    visited = [[False for _ in range(m)] for _ in range(n)]
    vcount = 0
    for i in range(len(virus)):
        vy, vx = virus[i]
        if visited[vy][vx]:
            continue
        visited[vy][vx] = True
        stack = [(vy, vx)]
        while stack:
            y, x = stack.pop()
            vcount += 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if ny >= n or ny < 0 or nx >= m or nx < 0 or board[ny][nx] == 1 or visited[ny][nx]:
                    continue
                stack.append((ny, nx))
                visited[ny][nx] = True
    
    answer = max(answer, len(virus) + len(clean) - 3 - vcount)


def solution(s, result):
    depth = len(result)
    if depth == 3:
        check()
        return
    for i in range(s, len(clean)):
        y, x = clean[i]
        board[y][x] = 1
        result.append(i)
        solution(i + 1, result)
        result.pop()
        board[y][x] = 0

solution(0, [])
print(answer)