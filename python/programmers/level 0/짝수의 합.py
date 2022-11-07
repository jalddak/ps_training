def solution(n):
    answer = 0
    i = 1
    while i*2 <= n:
        answer += i*2
        i += 1
    return answer