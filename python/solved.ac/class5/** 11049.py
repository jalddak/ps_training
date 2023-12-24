import sys
input = sys.stdin.readline

N = int(input())

ps = [list(map(int, input().split())) for _ in range(N)]
board = [[0 for _ in range(N)] for _ in range(N)]

for t in range(1, N):
    for s in range(N):
        if s + t == N: break
        board[s][s+t] = int(1e9)
        for j in range(s, s+t):
            board[s][s+t] = min(board[s][s+t], board[s][j] + board[j+1][s+t] + ps[s][0]*ps[j][1]*ps[s+t][1])
            
print(board[0][-1])