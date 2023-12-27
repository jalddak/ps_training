N = int(input())

import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(N)]

import heapq
heapq.heapify(nums)

result = 0
temp = heapq.heappop(nums)
while nums:
    if nums:
        heapq.heappush(nums, temp)
        temp = heapq.heappop(nums) + heapq.heappop(nums)
    result += temp

print(result)
