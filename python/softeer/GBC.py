import sys

n, m = map(int, input().split())
limits = []
for _ in range(n):
    term, speed = map(int, input().split())
    limits += [speed for _ in range(term)]

loca = 0
result = 0
for _ in range(m):
    term, speed = map(int, input().split())
    for i in range(term):
        if limits[loca] < speed:
            result = max(result, speed - limits[loca])
        loca += 1

print(result)