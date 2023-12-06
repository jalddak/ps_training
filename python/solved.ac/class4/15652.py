N, M = map(int, input().split())

def recursion(number, result):
    if len(result) == M:
        for n in result:
            print(n, end=' ')
        print()
    else:
        for n in range(number, N+1):
            recursion(n, result[:] + [n])

recursion(1, [])