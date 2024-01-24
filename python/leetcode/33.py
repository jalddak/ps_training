from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        minIndex = l
        nums = nums[minIndex:] + nums[:minIndex]

        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                return m + minIndex if m + minIndex < len(nums) else m + minIndex - len(nums)
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        setNums = set(nums)
        if target in setNums:
            return nums.index(target)
        return -1

