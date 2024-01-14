import sys
input = sys.stdin.readline

N, H = map(int, input().split())

td = []
dt = []
for i in range(N):
    if i % 2 == 0:
        dt.append(int(input()))
    else:
        td.append(int(input()))

td.sort()
dt.sort()

def carc_count(l):
    h = 0
    n = 0
    destroy = [0 for _ in range(H)]
    while h < H and n < len(l):
        if l[n] > h:
            destroy[h] = len(l) - n
            n -= 1
            h += 1
        n += 1
    return destroy

td_count = carc_count(td)
td_count.reverse()
dt_count = carc_count(dt)

min_b = N
cnt = 0
for i in range(H):
    count = td_count[i] + dt_count[i]
    if count < min_b:
        min_b = count
        cnt = 1
    elif count == min_b:
        min_b = count
        cnt += 1

print(min_b, cnt)