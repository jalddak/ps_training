s, e = map(int, input().split())

import heapq
heap = [[0, s]]
visited = [False for _ in range(100001)]

while heap:
    t, x = heapq.heappop(heap)
    visited[x] = True
    if x == e:
        print(t)
        break
    nums = [2 * x, x - 1, x + 1]
    for i in range(3):
        nt = t if i == 0 else t + 1
        num = nums[i]
        if num > 100000 or num < 0 or visited[num]:
            continue
        heapq.heappush(heap, [nt, num])

# visited -> check

s, e = map(int, input().split())

import heapq
heap = [[0, s]]
check = [100001 for _ in range(100001)]
check[s] = 0

while heap:
    t, x = heapq.heappop(heap)
    if x == e:
        print(t)
        break
    nums = [2 * x, x - 1, x + 1]
    for i in range(3):
        nt = t if i == 0 else t + 1
        num = nums[i]
        if num > 100000 or num < 0 or check[num] <= nt:
            continue
        heapq.heappush(heap, [nt, num])
        check[num] = nt