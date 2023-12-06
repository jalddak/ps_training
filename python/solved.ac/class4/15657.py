N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def recursion(index, result):
    if len(result) == M:
        for n in result:
            print(n, end=' ')
        print()
    else:
        for i in range(index, N):
            recursion(i, result[:] + [A[i]])

recursion(0, [])