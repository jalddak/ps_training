from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[:-1]
        nums2 = nums[1:]
        return max(dpCheck(nums1), dpCheck(nums2))

def dpCheck(nums):
    dp = [nums[0], max(nums[:2])]
    for i in range(2, len(nums)):
        dp.append(max(dp[i-2] + nums[i], dp[i-1]))
    return dp[-1]