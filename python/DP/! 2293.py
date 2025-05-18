n, k = list(map(int, input().split()))

coins = [int(input()) for _ in range(n)]

coins.sort()

board = [0 for _ in range(k+1)]
board[0] = 1
for i in range(n):
    for j in range(1, k+1):
        if j >= coins[i]:
            board[j] += board[j-coins[i]]

print(board[-1])