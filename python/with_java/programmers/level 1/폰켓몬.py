def solution(nums):
    length = len(nums)
    can = length//2
    nums = set(nums)
    return min(len(nums), can)