from typing import List

# 매우 느린 방법 - 안좋은 것 같음
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = set([0])
        stack = [0]
        while stack:
            loca = stack.pop()
            if loca >= len(nums):
                continue
            if loca == len(nums)-1:
                return True
            for n in range(1, nums[loca]+1):
                if loca + n not in visited:
                    visited.add(loca + n)
                    stack.append(loca + n)
        return False
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        loca = 0
        jump = nums[0]
        while loca < jump and loca < len(nums)-1:
            loca += 1
            jump = max(jump, loca + nums[loca])
        
        if loca == len(nums)-1:
            return True

        return False