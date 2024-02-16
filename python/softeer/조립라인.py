import sys

N = int(input())

ti = [list(map(int, input().split())) for _ in range(N-1)]
ant, bnt = map(int, input().split())

if N == 1:
    print(min(ant, bnt))
    exit()

dp = [(ti[0][0], ti[0][1])]
n = 1
while n < N-1:
    at, bt = dp.pop()
    ait, bit = ti[n][0], ti[n][1]
    abt, bat = ti[n-1][2], ti[n-1][3]
    nat = min(at + ait, bt + bat + ait)
    nbt = min(bt + bit, at + abt + bit)
    dp.append((nat, nbt))
    n += 1

at, bt = dp.pop()
abt, bat = ti[n-1][2], ti[n-1][3]
print(min(at + ant, at + abt + bnt, bt + bnt, bt + bat + ant))