graph = [[0, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 0 ,0],
         [0, 0, 1, 1, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 1, 1, 0]]

mod = 1000000007

def matrix_multi(a, b):
    result = [[0 for _ in range(8)] for _ in range(8)]

    for r in range(8):
        for i in range(8):
            for j in range(8):
                result[i][j] += (a[i][r] * b[r][j])
                result[i][j] %= mod

    return result

def solution(n):
    if n == 1:
        return graph
    elif n % 2 == 0:
        ban = solution(n//2)
        return matrix_multi(ban, ban)
    else:
        ban = solution(n//2)
        return matrix_multi(matrix_multi(ban, ban), graph)

D = int(input())
print(solution(D)[0][0])