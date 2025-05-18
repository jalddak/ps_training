tcCnt = 10

answer = []

def check(board, start):
    result = 1
    x = start
    y = 0
    while y < 100:
        if x - 1 >= 0 and board[y][x-1] == 1:
            while x - 1 >= 0 and board[y][x-1] == 1:
                x -= 1
                result += 1
        elif x + 1 < 100 and board[y][x+1] == 1:
            while x + 1 < 100 and board[y][x+1] == 1:
                x += 1
                result += 1
        y += 1
        result += 1


    return result


for _ in range(1, tcCnt + 1):
    tc = int(input())
    sb = "#" + str(tc) + " "
    board = [list(map(int, input().split())) for _ in range(100)]

    result = -1
    min_t = 10000
    for i in range(100):
        if board[0][i] == 0:
            continue
        candidate = check(board, i)
        if candidate < min_t:
            min_t = candidate
            result = i
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)