def solution(s):
    s = [int(l) for l in s.split()]
    big = str(max(s))
    small = str(min(s))
    return small + ' ' + big