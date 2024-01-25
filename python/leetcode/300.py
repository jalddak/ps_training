from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            if num > dp[-1]:
                dp.append(num)
            else:
                dp[bs(dp, num)] = num
        return len(dp)

def bs(dp, num):
    l, r = 0, len(dp)-1
    while l <= r:
        m = (l+r) // 2
        if dp[m] == num:
            return m
        elif dp[m] < num:
            l = m + 1
        else:
            r = m - 1
    return l
