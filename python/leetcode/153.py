from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        result = nums[0]
        while l <= r:
            m = (l+r) // 2
            result = min(result, nums[l], nums[m], nums[r])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return result


print(Solution.findMin(Solution, [3,4,5,1,2]))