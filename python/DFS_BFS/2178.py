# bfs
from collections import deque


N, M = list(map(int, input().split()))

board = []
for _ in range(N):
    row = []
    string = input()
    for char in string:
        row.append(char)
    row = list(map(int, row))
    board.append(row)

visited = [[False for _ in range(M)] for _ in range(N)]


def main():
    global N, M, board, visited
    queue = deque([[0, 0, 1]])

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while len(queue) != 0:
        y, x, cnt = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            ncnt = cnt + 1
            if ny == N-1 and nx == M-1:
                print(ncnt)
                return ncnt
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append([ny, nx, ncnt])


if __name__ == '__main__':
    main()