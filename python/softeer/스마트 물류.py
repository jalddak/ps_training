import sys
input = sys.stdin.readline

N, K = map(int, input().split())
info = []
for command in list(input()):
    info.append(0 if command=='H' else 1)

result = 0
for i in range(N):
    c = info[i]
    if c == 0 or c == 2:
        continue
    for r in range(-K, K+1):
        if i + r < 0:
            continue
        if i + r >= N:
            break
        if info[i+r] == 0:
            info[i+r] = 2
            result += 1
            break

print(result)