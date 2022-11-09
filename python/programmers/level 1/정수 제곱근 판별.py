def solution(n):
    x = n ** 0.5
    if x % int(x) == 0:
        return (x+1) ** 2
    else:
        return -1