from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))
        return dp[-1]