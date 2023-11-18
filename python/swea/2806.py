T = int(input())
result = 0

def nqueen(index, N, check):
    global result
    if index == N:
        result += 1
    for i in range(N):
        flag = False
        for j in range(index):
            if check[j] == i or abs(index - j) == abs(i - check[j]):
                flag = True
                break
        if not flag:
            check[index] = i
            nqueen(index + 1, N, check)

for round in range(1, T+1):
    result = 0
    rstr = "#" + str(round) + " "
    N = int(input())

    check = [-1 for _ in range(N)]
    nqueen(0, N, check)
    print(rstr + str(result))
