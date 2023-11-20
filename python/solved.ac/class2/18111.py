N, M, B = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

block_num = B
min_h = 256
for i in range(N):
    block_num += sum(board[i])
    min_h = min(min_h, min(board[i]))

max_h = min(256, block_num // (N*M))

result = -1
for h in range(min_h, max_h+1):
    time = 0
    for i in range(N):
        for j in range(M):
            if h > board[i][j]:
                time += h - board[i][j]
            elif h < board[i][j]:
                time += -2 * (h - board[i][j])
    if result == -1:
        result = [time, h]
    elif time > result[0]:
        break
    elif time <= result[0]:
        result = [time, h]

print(result[0], result[1])
