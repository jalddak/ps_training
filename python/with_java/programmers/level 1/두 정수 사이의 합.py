def solution(a, b):
    answer = 0
    big = max(a, b)
    small = min(a, b)
    for n in range(small, big+1):
        answer += n
    return answer