import sys

m, n, k = map(int, input().split())
scmd = list(map(int, input().split()))
cmd = list(map(int, input().split()))

current = 0
result = False
for i in range(n-m+1):
    if scmd == cmd[i:i+m]:
        result = True

if result:
    print('secret')
else:
    print('normal')