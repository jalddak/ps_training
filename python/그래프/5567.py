import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

l = [list(map(int, input().split())) for _ in range(m)]

friends = set()
for i in range(m):
    v1, v2 = l[i]
    if v1 == 1:
        friends.add(v2)
    if v2 == 1:
        friends.add(v1)

ffrineds = set()
for i in range(m):
    v1, v2 = l[i]
    if v1 in friends and v2 != 1:
        ffrineds.add(v2)
    if v2 in friends and v1 != 1:
        ffrineds.add(v1)

print(len(friends | ffrineds))