def solution(n, left, right):
    answer = []
    for num in range(left, right+1):
        result = num % n + 1 if num // n < num % n else num // n + 1
        answer.append(result)
    return answer