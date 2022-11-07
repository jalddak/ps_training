def solution(numbers):
    answer = 0
    오름차순 = sorted(numbers)
    내림차순 = sorted(numbers, reverse = True)
    answer = max(오름차순[0] * 오름차순[1], 내림차순[0] * 내림차순[1])
    return answer