dx = [-1, 1]

answer = []
for _ in range(10):
    tc = int(input())
    result = "#" + str(tc) + " "

    board = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    x = board[y].index(2)

    while y > 0:
        for d in range(2):
            nx = x + dx[d]
            if nx < 0 or nx > 99 or board[y][nx] == 0:
                continue
            while 0 <= nx < 100 and board[y][nx] == 1:
                x = nx
                nx = x + dx[d]
            break
        y -= 1
    result += str(x)
    answer.append(result)

for a in answer:
    print(a)