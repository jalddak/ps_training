def solution(nums):
    answer = 0
    length = len(nums)
    cnt = length//2
    result = []
    
    for n in nums:
        if n not in result:
            result.append(n)
            answer += 1
        if answer == cnt:
            break
    
    return answer