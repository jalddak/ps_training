import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

star = ""
for _ in range(n):
    star += "*"

for _ in range(m):
    print(star)