n, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def divide(num):
    if num == 1:
        return board
    half = num // 2
    result = divide(half)
    result = calc(result, result)
    if num % 2 == 1:
        result = calc(result, board)
    return result

def calc(one, two):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += one[i][k] * two[k][j]
            result[i][j] %= 1000

    return result

result = divide(b)
for r in result:
    print(" ".join(map(str, map(lambda x: x%1000, r))))