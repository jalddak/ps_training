# 재귀

import sys
sys.setrecursionlimit(10**6)

N = int(input())

board = [[' ' for _ in range(2*N)] for _ in range(N)]

def recursion(y, x, n):
    if n == 3:
        board[y][x] = '*'
        board[y+1][x-1] = '*'
        board[y+1][x+1] = '*'
        for d in range(-2, 3):
            board[y+2][x+d] = '*'

    else:
        ban = n // 2
        recursion(y, x, ban)
        recursion(y+ban, x-ban, ban)
        recursion(y+ban, x+ban, ban)


recursion(0, N-1, N)
for row in board:
    print("".join(row))