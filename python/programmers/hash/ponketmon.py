def solution(nums):
    answer = 0
    kinds_dict = {}
    for num in nums:
        if num not in kinds_dict:
            kinds_dict[num] = 0
            answer += 1
        if answer >= len(nums)/2:
            break
    return answer