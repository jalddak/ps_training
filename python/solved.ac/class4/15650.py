N, M =  map(int, input().split())

results = []
def recursion(num, result):
    if len(result) == M:
        results.append(result)
    for n in range(num, N+1):
        next = result[:]
        next.append(n)
        recursion(n + 1, next)

recursion(1, [])

for result in results:
    result = map(str, result)
    print(" ".join(result))