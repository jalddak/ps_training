# DFS

M, N = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(M)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[0 for _ in range(N)] for _ in range(M)]

def dfs(y, x):
    global dy, dx, M, N
    result = 0
    if y == M-1 and x == N-1:
        visited[y][x] = 1
        return visited[y][x]

    check = False
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < M and 0 <= nx < N and board[y][x] > board[ny][nx]:
            if visited[ny][nx] == 0:
                if dfs(ny, nx) != -1:
                    result += visited[ny][nx]
                    check = True
            elif visited[ny][nx] != -1:
                result += visited[ny][nx]
                check = True

    if not check:
        result = -1
    visited[y][x] = result
    return result

if __name__ == '__main__':
    dfs(0, 0)
    if visited[0][0] == -1:
        print(0)
    else:
        print(visited[0][0])