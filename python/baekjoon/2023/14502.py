# visited 관련 코드 다 빼는게 더 빠름

first_row = list(map(int, input().split()))
n = first_row[0]
m = first_row[1]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]
result = 0

def spread():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    global n, m, board, result
    bc = [[0 for _ in range(m)] for _ in range(n)]
    virus_c = []
    for i in range(n):
        for j in range(m):
            bc[i][j] = board[i][j]
            if bc[i][j] == 2:
                virus_c.append([i,j])
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
    safe = 0
    for i in range(n):
        for j in range(m):
            if bc[i][j] == 0:
                safe += 1
    result = max(result, safe)

def make_wall(depth):
    visited_coord = []
    check = []
    
    global n, m, board, visited
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and visited[i][j] == 0:
                board[i][j] = 1
                if depth + 1 > 3:
                    spread()
                else:
                    visited_coord += make_wall(depth + 1)
                    for v in visited_coord:
                        visited[v[0]][v[1]] = 0
                board[i][j] = 0
                visited[i][j] = 1
                check.append([i, j])
    
    return check

if __name__ == '__main__':
    make_wall(1)
    print(result)
