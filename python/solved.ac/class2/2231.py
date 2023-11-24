N = int(input())

for n in range(N):
    nstr = str(n)
    ts = 0
    for s in nstr:
        ts += int(s)
    c = n + ts
    if c == N:
        print(n)
        exit()

print(0)