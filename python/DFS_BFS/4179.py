# BFS

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

blocked = [[0 for _ in range(C)] for _ in range(R)]
fire = []
jihun = []

for i in range(R):
    for j in range(C):
        if board[i][j] == '#':
            blocked[i][j] = 1
        if board[i][j] == 'F':
            fire.append((i, j))
            blocked[i][j] = 2
        if board[i][j] == 'J':
            jihun.append((i, j))

def main():
    global jihun, fire
    cnt = 0
    escape = False
    while len(jihun) != 0 and not escape:
        fire, x = bfs('F', fire)
        jihun, escape = bfs('J', jihun)
        cnt += 1
    if escape:
        print(cnt)
    else:
        print("IMPOSSIBLE")


def bfs(what, before):
    global dy, dx, R, C, board, blocked
    after = []
    for y, x in before:
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < R and 0 <= nx < C:
                if what == 'J' and blocked[ny][nx] == 0:
                    after.append((ny, nx))
                    blocked[ny][nx] = 3
                if what == 'F' and blocked[ny][nx] not in [1, 2]:
                    after.append((ny, nx))
                    blocked[ny][nx] = 2
            else:
                if what == 'J':
                    return after, True
    return after, False
            

if __name__ == '__main__':
    main()