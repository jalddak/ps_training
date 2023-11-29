import sys
input = sys.stdin.readline

N, M = map(int, input().split())

d = {}
for _ in range(N):
    site, pwd = input().split()
    d[site] = pwd

for _ in range(M):
    print(d[input()[:-1]])