from itertools import combinations

first_row = list(map(int, input().split()))
n = first_row[0]
m = first_row[1]

board = []
f_virus = []
cleans = []

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 0:
            cleans.append([i, j])
        if board[i][j] == 2:
            f_virus.append([i,j])

cleans = list(combinations(cleans, 3))

result = 0

def safe_check(bc):
    global result
    safe = 0
    for i in range(n):
        for j in range(m):
            if bc[i][j] == 0:
                safe += 1
    result = max(result, safe)

def spread(bc):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    global n, m, f_virus
    virus_c = f_virus[:]
    while len(virus_c) != 0:
        virus = virus_c.pop()
        y = virus[0]
        x = virus[1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny >= 0 and ny < n and nx >= 0 and nx < m:
                if bc[ny][nx] == 0:
                    bc[ny][nx] = 2
                    virus_c.append([ny, nx])
    safe_check(bc)

def make_wall():
    global n, m, board, cleans
    for clean in cleans:
        bc = []
        for i in range(n):
            bc.append(board[i][:])
        for c in clean:
            bc[c[0]][c[1]] = 1
        spread(bc)
        

if __name__ == '__main__':
    make_wall()
    print(result)
