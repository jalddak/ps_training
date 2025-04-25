answer = []

for _ in range(10):
    tc = int(input())
    format = "#" + str(tc) + " "
    result = 0

    board = [list(map(int, input().split())) for _ in range(100)]

    diagSum = 0
    antiDiagSum = 0
    for i in range(100):
        rowSum = 0
        colSum = 0
        for j in range(100):
            rowSum += board[i][j]
            colSum += board[j][i]
            if i == j:
                diagSum += board[i][j]
            if i + j == 99:
                antiDiagSum += board[i][j]
        result = max(rowSum, colSum, result)
    result = max(diagSum, antiDiagSum, result)

    format += str(result)
    answer.append(format)

for a in answer:
    print(a)