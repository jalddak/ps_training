# BFS
from collections import deque

board = [list(input()) for _ in range(12)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def main():
    global board
    result = 0
    while bfs(board):
        drop(board)
        result += 1
    return result


def bfs(board):
    global dy, dx
    visited = [[False for _ in range(6)] for _ in range(12)]
    result = False
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and visited[i][j] == False:
                color = board[i][j]
                report = []
                queue = deque([[i, j]])
                visited[i][j] = True
                while len(queue) != 0:
                    y, x = queue.popleft()
                    report.append((y, x))
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < 12 and 0 <= nx < 6 and not visited[ny][nx] and board[ny][nx] == color:
                            visited[ny][nx] = True
                            queue.append([ny, nx])
                if len(report) >= 4:
                    result = True
                    for y, x in report:
                        board[y][x] = '.'
            else:
                visited[i][j] = True
    
    return result

def drop(board):
    for col in range(6):
        for i in range(11, -1, -1):
            if board[i][col] == ".":
                for j in range(i, -1, -1):
                    if board[j][col] != ".":
                        board[i][col], board[j][col] = board[j][col], board[i][col]
                        break

if __name__ == "__main__":
    print(main())