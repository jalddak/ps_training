# 첫번째 방법
import sys

input = sys.stdin.readline

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

def calc_dist(one, two):
    return ((one[0] - two[0]) ** 2 + (one[1] - two[1]) ** 2) ** 0.5

result = 0
visited = set()
heap = [(0, 0)]

import heapq

while len(visited) <= n - 1:
    dist, index = heapq.heappop(heap)
    if index in visited:
        continue
    visited.add(index)
    result += dist
    for i in range(n):
        if i not in visited:
            n_dist = calc_dist(stars[index], stars[i])
            # heapq.heappush(heap, n_dist) << 실수했던 부분
            heapq.heappush(heap, (n_dist, i))

print(format(result, ".2f"))

# 두번째 방법 (1번째 방법 heappush 에서 잘못해서 오류나가지고 억지로 sort 하는 걸로 구현했는데 그럴 이유 없었음)
import sys
input = sys.stdin.readline

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]


visited = [False for _ in range(n)]
count = 0
stack = [(0, 0)]
result = 0

def calc_dist(one, two):
    return (one[0] - two[0]) ** 2 + (one[1] - two[1]) ** 2

while len(stack) != 0 and count < n:
    dist, index = stack.pop()
    if visited[index]:
        continue
    result += dist ** 0.5
    visited[index] = True
    count += 1
    for i in range(n):
        if visited[i]:
            continue
        n_dist = calc_dist(stars[index], stars[i])
        stack.append((n_dist, i))
        stack.sort(key=lambda x:-x[0])

print(format(result, ".2f"))