import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dbj = {}

for _ in range(N):
    dbj[input()[:-1]] = 1

for _ in range(M):
    bj = input()[:-1]
    if bj in dbj:
        dbj[bj] += 1
    
result = []
for key in dbj:
    if dbj[key] == 2:
        result.append(key)

result.sort()
print(len(result))

for name in result:
    print(name)