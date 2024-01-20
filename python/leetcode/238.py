from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        length = len(nums)
        for i in range(1, length):
            left.append(left[-1]*nums[i-1])
            right.append(right[-1]*nums[length-i])
        right.reverse()
        result = []
        for i in range(length):
            result.append(left[i]*right[i])
        return result