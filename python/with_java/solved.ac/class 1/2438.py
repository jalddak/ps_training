import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    s = ""
    for _ in range(i):
        s += "*"
    print(s)