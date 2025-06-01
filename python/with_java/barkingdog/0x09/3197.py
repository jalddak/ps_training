import sys
def input():
    return sys.stdin.readline().strip()

def init(r, c, board, visited, melts, ducks, dy, dx):
    for i in range(r):
        for j in range(c):
            if board[i][j] == "L":
                ducks.append((i, j))
            if board[i][j] == "X" or visited[i][j][0] != -1:
                continue
            visited[i][j] = (i, j)
            stack = [(i, j)]
            while stack:
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny >= r or ny < 0 or nx >= c or nx < 0 or visited[ny][nx][0] != -1:
                        continue
                    visited[ny][nx] = visited[y][x]
                    if board[ny][nx] == "X":
                        melts.append((ny, nx))
                        continue
                    stack.append((ny, nx))

def uf(visited, coord):
    y, x = coord
    if visited[y][x] != (y, x):
        visited[y][x] = uf(visited, visited[y][x])
    return visited[y][x]
    

def solution(r, c, board, visited, melts, ducks, dy, dx):
    result = 0
    while True:
        ducks[0] = uf(visited, ducks[0])
        ducks[1] = uf(visited, ducks[1])
        if ducks[0] == ducks[1]:
            break

        result += 1
        next = []
        while melts:
            y, x = melts.pop()
            board[y][x] = "."
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if ny >= r or ny < 0 or nx >= c or nx < 0 or (visited[ny][nx][0] != -1 and uf(visited, (ny, nx)) == uf(visited, (y, x))):
                    continue
                if board[ny][nx] == "X" and visited[ny][nx][0] != -1:
                    continue
                if board[ny][nx] == "X":
                    visited[ny][nx] = visited[y][x]
                    next.append((ny, nx))
                    continue
                visited[visited[ny][nx][0]][visited[ny][nx][1]] = visited[y][x]
        melts = next

    print(result)

def main():
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]
    visited = [[(-1, -1) for _ in range(c)] for _ in range(r)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    melts = []
    ducks = []
    init(r, c, board, visited, melts, ducks, dy, dx)
    solution(r, c, board, visited, melts, ducks, dy, dx)

if __name__ == "__main__":
    main()