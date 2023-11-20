N = int(input())

for n in range(N):
    nstr = str(n)
    ts = 0
    for s in nstr:
        ts += int(s)
    c = n + ts
    print(c, n)
    if c == N:
        print(c)
        exit()

print(0)