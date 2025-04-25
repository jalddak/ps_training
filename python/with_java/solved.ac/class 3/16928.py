import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [-1 for _ in range(101)]
ls = dict()
for _ in range(n + m):
    s, e = map(int, input().split())
    ls[s] = e

from collections import deque
q = deque([1])
board[1] = 0

while(q):
    x = q.popleft()
    for i in range(1, 7):
        nx = x + i
        if nx in ls:
            nx = ls[nx]
        if board[nx] == -1 or board[nx] > board[x] + 1:
            q.append(nx)
            board[nx] = board[x] + 1
            if nx == 100:
                print(board[nx])
                exit()
