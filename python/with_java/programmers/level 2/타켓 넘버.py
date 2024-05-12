def solution(numbers, target):
    dp = [0]
    for n in numbers:
        dp = list(map(lambda x:x-n, dp)) + list(map(lambda x:x+n, dp))
    
    answer = 0
    for n in dp:
        if n == target:
            answer += 1
    
    return answer