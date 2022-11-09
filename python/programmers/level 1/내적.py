def solution(a, b):
    answer = 0
    length = len(a)
    for index in range(length):
        answer += a[index] * b[index]
    return answer