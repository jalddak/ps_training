def solution(nums):
    answer = 0
    length = len(nums)/2
    set_nums = set(nums)
    s_len = len(set_nums)
    if s_len > length :
        answer = length
    else:
        answer = s_len
    return answer