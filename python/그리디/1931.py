import sys
input = sys.stdin.readline

n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]

l.sort(key = lambda x:(x[1], x[0]))

result = 0
temp = 0

for s, e in l:
    if s >= temp:
        temp = e
        result += 1

print(result)