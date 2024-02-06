from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort(reverse=True)
        before = nums.pop()
        cnt = 1
        result = 1

        while nums:
            num = nums.pop()
            if num == before + 1:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 1
            before = num
        result = max(result, cnt)
        return result