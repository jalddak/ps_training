from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(max(result[-1]+nums[i], nums[i]))
        return max(result)