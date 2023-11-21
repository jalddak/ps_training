import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dogam = {}
dogam2 = {}

for i in range(1, N+1):
    name = input()[:-1]
    dogam[i] = name
    dogam2[name] = i

for j in range(M):
    q = input()[:-1]
    if q.isdigit():
        print(dogam.get(int(q)))
    else:
        print(dogam2.get(q))