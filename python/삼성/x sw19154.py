# import sys
# input = sys.stdin.readline

# T = int(input())

# result = []
# for _ in range(T):
#     N = int(input())
#     loses = []
#     for _ in range(N):
#         nums = list(map(int, input().split()))
#         scores = []
#         for n in nums:
#             scores.append(sum(nums)-n)
#         loses.append(scores)
#     if N < 3:
#         result.append(-1)
#         continue

#     total = 0
#     balance = [set(), set(), set()]
#     for index in range(N):
#         min_s = -1
#         min_i = -1
#         scores = loses[index]
#         for i in range(3):
#             if min_s > scores[i] or min_s == -1:
#                 min_s = scores[i]
#                 min_i = i
#         total += min_s
#         balance[min_i].add(index)
#     print(total, balance)

import sys
input = sys.stdin.readline

T = int(input())

import heapq
result = []
for _ in range(T):
    N = int(input())
    loses = []
    for _ in range(N):
        nums = list(map(int, input().split()))
        scores = []
        for n in nums:
            scores.append(sum(nums)-n)
        loses.append(scores)
    if N < 3:
        result.append(-1)
        continue

    heap = [(0, [0, set()])]
    while heap:
        total, info = heapq.heappop(heap)
        cnt, balance = info
        if cnt == N and len(balance) == 3:
            result.append(total)
            break
        if cnt == N:
            continue
        for i in range(3):
            heapq.heappush(heap, (total+loses[cnt][i], [cnt+1, balance | set([i])]))

for r in result:
    print(r)