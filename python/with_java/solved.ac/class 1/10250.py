t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    flag = 1 if n % h == 0 else 0
    floor = n % h + (h if flag else 0)
    rnum = 1 + n // h - (1 if flag else 0)

    srn = str(rnum)
    if rnum < 10:
        srn = '0' + srn
    print(str(floor) + srn)