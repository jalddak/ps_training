def solution(n):
    루트값 = n ** 0.5
    if 루트값 % int(루트값) == 0:
        return 1
    else:
        return 2