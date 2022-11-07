def solution(n):
    answer = 0
    for num in range(4, n+1):
        for i in range(2, num):
            if num % i == 0:
                answer += 1
                break
    return answer