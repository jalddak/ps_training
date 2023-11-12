# bfs

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(before, h, w, target):
    global dy, dx, board
    after = []
    while len(before) != 0:
        y, x = before.pop()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < h and 0 <= nx < w:
                if target == '*' and board[ny][nx] in ['.', '@']:
                    board[ny][nx] = target
                    after.append((ny, nx))
                elif target == '@' and board[ny][nx] == '.':
                    board[ny][nx] = target
                    after.append((ny, nx))
            elif target == '@':
                after = [(-1, -1)]
                return after
    
    return after

for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    fire = []
    sangun = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire.append((i, j))
            elif board[i][j] == '@':
                sangun.append((i, j))
    
    result = 0
    while True:
        result += 1
        fire = bfs(fire, h, w, '*')
        sangun = bfs(sangun, h, w, '@')
        if len(sangun) == 0:
            print("IMPOSSIBLE")
            break
        elif sangun[0] == (-1, -1):
            print(result)
            break