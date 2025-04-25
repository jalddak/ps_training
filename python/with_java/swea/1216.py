tcCnt = 10

answer = []

def dp(row):
    board = [[True for _ in range(100)] for _ in range(100)]

    result = 1
    for i in range(1, 100):
        for j in range(100 - i):
            if row[j] != row[j + i] or not board[j+1][j+i-1]:
                board[j][j+i] = False
                continue
            result = max(result, i + 1)
    return result

for tc in range(1, tcCnt+1):
    tcNum = int(input())
    sb = "#" + str(tc) + " "

    board = [list(input()) for _ in range(100)] + [[] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            board[100 + j].append(board[i][j])

    result = 0
    for i in range(200):
        result = max(result, dp(board[i]))
    
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)