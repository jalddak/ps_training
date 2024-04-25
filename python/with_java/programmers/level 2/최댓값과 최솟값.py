def solution(s):
    s = list(map(int, s.split()))
    big = str(max(s))
    small = str(min(s))
    return small + ' ' + big