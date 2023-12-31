import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

board = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1].append((s, d, z))

def catch(c):
    global board, R
    for r in range(R):
        if board[r][c]:
            s, d, z = board[r][c].pop()
            return z
    return 0

def shark_move():
    global board, R, C
    after = []
    for r in range(R):
        for c in range(C):
            if board[r][c]:
                s, d, z = board[r][c].pop()
                nr, nc = r, c
                for _ in range(s):
                    nr += dy[d]
                    nc += dx[d]
                    if 0 <= nr < R and 0 <= nc < C:
                        continue
                    if d % 2 == 0:
                        d -= 1
                    else:
                        d += 1
                    nr += 2*dy[d]
                    nc += 2*dx[d]
                after.append((nr, nc, s, d, z))
    
    for r, c, s, d, z in after:
        if not board[r][c] or (board[r][c] and board[r][c][0][2] < z):
            board[r][c] = [(s, d, z)]
        
result = 0
for c in range(C):
    result += catch(c)
    shark_move()

print(result)


