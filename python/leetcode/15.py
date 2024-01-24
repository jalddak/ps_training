from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()

        result = set()
        for i in range(n-2):
            f = nums[i]
            target = -f
            sub = nums[i+1:]
            l, r = 0, len(sub)-1
            while l < r:
                if sub[l] + sub[r] == target:
                    result.add((f, sub[l], sub[r]))
                    jump = 1
                    while l+jump < len(sub) and sub[l] == sub[l + jump]:
                        jump += 1
                    l += jump
                elif sub[l] + sub[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(result)
    

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()

        result = set()
        for i in range(n-2):
            f = nums[i]
            target = -f
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((f, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return result
    
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()

        result = set()
        for i in range(n-2):
            f = nums[i]
            target = -f
            l, r = i+1, len(nums)-1
            while l < r:
                candidate = nums[l] + nums[r]
                if candidate == target:
                    result.add((f, nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif candidate < target:
                    l += 1
                else:
                    r -= 1
        return result