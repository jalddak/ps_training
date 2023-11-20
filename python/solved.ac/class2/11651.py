import sys
input = sys.stdin.readline

N = int(input())

l = [tuple(map(int, input().split())) for _ in range(N)]

l.sort(key = lambda x:(x[1], x[0]))

for x, y in l:
    print(x, y)