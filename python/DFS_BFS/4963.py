# DFS

def dfs(M, N):
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    stack = []
    cnt = 0

    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                stack.append([i, j])
                visited[i][j] = True
                cnt += 1
            while len(stack) != 0:
                y, x = stack.pop()
                for d in range(8):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and board[ny][nx] == 1:
                        stack.append([ny, nx])
                        visited[ny][nx] = True
    return cnt

if __name__ == '__main__':
    while True:
        M, N = list(map(int, input().split()))
        if M == 0 and N == 0:
            exit()
        print(dfs(M, N))