import sys
input = sys.stdin.readline

while True:
    s,m,h = sorted(list(map(int, input().split())))
    if s == 0 and m == 0 and h == 0:
        break
    if s ** 2 + m ** 2 == h ** 2:
        print("right")
    else:
        print("wrong")
