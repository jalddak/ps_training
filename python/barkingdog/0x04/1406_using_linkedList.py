import sys
def input(): return sys.stdin.readline().rstrip()

INF = 600001
data = ["" for _ in range(INF)]
prev = [-1 for _ in range(INF)]
next = [-1 for _ in range(INF)]

unUsed = 1

s = input()
for a in s:
    data[unUsed] = a
    prev[unUsed] = unUsed - 1
    next[unUsed - 1] = unUsed
    unUsed += 1

cursor = unUsed - 1
m = int(input())
for _ in range(m):
    cmd = input().split()
    if cmd[0] == "L":
        cursor = prev[cursor] if prev[cursor] != -1 else cursor
    if cmd[0] == "D":
        cursor = next[cursor] if next[cursor] != -1 else cursor
    if cmd[0] == "B":
        if prev[cursor] == -1:
            continue
        prevIndex = prev[cursor]
        nextIndex = next[cursor]
        next[prevIndex] = nextIndex
        if nextIndex != -1:
            prev[nextIndex] = prevIndex
        cursor = prevIndex
    if cmd[0] == "P":
        data[unUsed] = cmd[1]
        prev[unUsed] = cursor
        next[unUsed] = next[cursor]
        prev[next[cursor]] = unUsed
        next[cursor] = unUsed
        unUsed += 1
        cursor = next[cursor]

answer = []
index = 0
while next[index] != -1:
    answer.append(data[index])
    index = next[index]
answer.append(data[index])
print("".join(answer))