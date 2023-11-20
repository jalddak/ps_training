import sys
input = sys.stdin.readline

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

l.sort(key=lambda x:(x[0], x[1]))

for x, y in l:
    print(x,y)