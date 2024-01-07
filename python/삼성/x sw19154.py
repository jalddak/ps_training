import sys
input = sys.stdin.readline

T = int(input())

from itertools import permutations

results = []
for _ in range(T):
    N = int(input())
    agents = [i for i in range(N)]
    candidates = list(map(list, list(permutations(agents, 3))))

    sum_loses = 0
    loses = []
    for _ in range(N):
        ability = list(map(int, input().split()))
        sum_ability = sum(ability)
        lose = []
        for i in range(3):
            lose.append(sum_ability-ability[i])
        sum_loses += min(lose)
        loses.append(lose)

    if N < 3:
        results.append(-1)
        continue

    result = N * (10**6) + 1
    for candidate in candidates:
        temp = sum_loses - min(loses[candidate[0]]) - min(loses[candidate[1]]) - min(loses[candidate[2]])
        temp += loses[candidate[0]][0] + loses[candidate[1]][1] + loses[candidate[2]][2]

        
        result = min(temp, result)
    results.append(result)

for r in results:
    print(r)


# 3
# 3
# 1 1 1
# 1 1 1
# 1 1 1
# 1
# 9 9 9
# 4
# 1 1 1
# 2 3 2
# 3 3 5
# 4 4 6    

# import sys
# input = sys.stdin.readline

# T = int(input())

# import heapq
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

#     heap = [(0, [0, set()])]
#     while heap:
#         total, info = heapq.heappop(heap)
#         cnt, balance = info
#         if cnt == N and len(balance) == 3:
#             result.append(total)
#             break
#         if cnt == N:
#             continue
#         for i in range(3):
#             heapq.heappush(heap, (total+loses[cnt][i], [cnt+1, balance | set([i])]))

# for r in result:
#     print(r)