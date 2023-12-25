# pypy 만 통과
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

# python 도 통과
first = input()
second = input()

board = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1] == second[j-1]:
            board[i][j] = board[i-1][j-1] + 1
        else:
            board[i][j] = max(board[i-1][j], board[i][j-1])


print(board[-1][-1])
stack = []
fn = len(first)
sn = len(second)
while len(stack) != board[-1][-1]:
    if board[fn][sn] == board[fn-1][sn]:
        fn -= 1
    elif board[fn][sn] == board[fn][sn-1]:
        sn -= 1
    else:
        stack.append(first[fn-1])
        fn -= 1
        sn -= 1
print("".join(reversed(stack)))