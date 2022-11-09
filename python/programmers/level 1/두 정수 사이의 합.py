def solution(a, b):
    big = 0
    small = 0
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
    answer = 0
    for i in range(small, big+1):
        answer += i
    return answer