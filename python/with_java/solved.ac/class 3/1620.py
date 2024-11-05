import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nameToIndex = dict()
indexToName = dict()
for i in range(1, n+1):
    name = input()[:-1]
    nameToIndex[name] = i
    indexToName[i] = name

for _ in range(m):
    ip = input()[:-1]
    if ip.isdigit():
        print(indexToName[int(ip)])
    else:
        print(nameToIndex[ip])