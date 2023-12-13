N, B = map(int, input().split())

A = [list(map(lambda x:x%1000, (map(int, input().split())))) for _ in range(N)]

def op(one, two):
    global N, A
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            element = 0
            for k in range(N):
                element += one[i][k] * two[k][j]
            row.append(element % 1000)
        result.append(row)
    return result
            

def solution(power):
    global N, A

    result = []
    for i in range(N):
        result.append(A[i])

    if power == 1:
        return result
    elif power % 2 == 0:
        ban = solution(power//2)
        return op(ban, ban)
    else:
        ban = solution(power//2)
        return op(op(ban, ban), result)

result = solution(B)
for r in result:
    r = map(str, r)
    print(" ".join(r))