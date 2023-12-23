first = input()
second = input()

board = [['' for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1] == second[j-1]:
            board[i][j] = board[i-1][j-1] + first[i-1]
        elif len(board[i][j-1]) >= len(board[i-1][j]):
            board[i][j] = board[i][j-1]
        else:
            board[i][j] = board[i-1][j]


length = len(board[-1][-1])
print(length)
if length:
    print(board[-1][-1])