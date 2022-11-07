def solution(sides):
    sides.sort()
    long = sides.pop()
    if long < sum(sides):
        return 1
    else:
        return 2