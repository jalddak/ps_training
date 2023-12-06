N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

result = []

def recursion(index, temp):
    if len(temp) == M:
        result.append(tuple(temp))
    else:
        for i in range(index, N):
            recursion(i, temp[:] + [A[i]])

recursion(0, [])

result = list(map(list, set(result)))
result.sort()

for l in result:
    for n in l:
        print(n, end=' ')
    print()
    
