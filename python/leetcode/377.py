from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        for t in range(target+1):
            for n in nums:
                if t-n > 0:
                    dp[t] += dp[t-n]
                if t-n == 0:
                    dp[t] += 1
        return dp[-1]