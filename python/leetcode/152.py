from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxDp = [nums[0]]
        minDp = [nums[0]]
        for i in range(1, len(nums)):
            temp = [maxDp[-1]*nums[i], minDp[-1]*nums[i], nums[i]]
            temp.sort()
            maxDp.append(temp[-1])
            minDp.append(temp[0])
        return max(maxDp)