# DFS or BFS

N = int(input())
board = [input() for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def good():
    global N, board, dy, dx

    visited = [[False for _ in range(N)] for _ in range(N)]
    stack = []
    result = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                stack.append([i, j])
                visited[i][j] = True
                result += 1
            while len(stack) != 0:
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and board[y][x] == board[ny][nx]:
                        visited[ny][nx] = True
                        stack.append([ny, nx])
    return result

def bad():
    global N, board, dy, dx

    visited = [[False for _ in range(N)] for _ in range(N)]
    stack = []
    result = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                stack.append([i, j])
                visited[i][j] = True
                result += 1
            while len(stack) != 0:
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                        if (board[y][x] in ['G', 'R'] and board[ny][nx] in ['G', 'R']) or board[y][x] == board[ny][nx]:
                            visited[ny][nx] = True
                            stack.append([ny, nx])
    return result

if __name__ == '__main__':
    print(good(), end = ' ')
    print(bad())