from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return broteForce(nums, target)
        return usingHashTable(nums, target)
    
def broteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def usingHashTable(nums, target):
    numMap = {}
    length = len(nums)
    for i in range(length):
        need = target - nums[i]
        if need in numMap:
            return [numMap[need], i]
        numMap[nums[i]] = i
    return []