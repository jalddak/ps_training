import sys
input = sys.stdin.readline

N = int(input())

hs = [tuple(map(int, input().split())) for _ in range(N)]

rank = [1 for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if hs[i][0] > hs[j][0] and hs[i][1] > hs[j][1]:
            rank[j] += 1
        elif hs[i][0] < hs[j][0] and hs[i][1] < hs[j][1]:
            rank[i] += 1

for n in rank:
    print(n, end=" ")