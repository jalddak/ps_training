N = int(input())
A = list(map(int, input().split()))

result = -1
from collections import deque
queue = deque([])
for i in range(N):
    visited = [False for _ in range(N)]
    visited[i] = True
    queue.append([0, i, visited])

while queue:
    n, before_i, visited = queue.popleft()
    check = True
    for i in range(N):
        n_visited = visited[:]
        if not visited[i]:
            n_visited[i] = True
            queue.append([n + abs(A[before_i] - A[i]), i, n_visited])
            check = False
    if check:
        result = max(result, n)
print(result)

N = int(input())
A = list(map(int, input().split()))
result = -1

from itertools import permutations
candidate = list(permutations(A, N))
for nums in candidate:
    temp = 0
    for i in range(1, N):
        temp += abs(nums[i-1] - nums[i])
    result = max(result, temp)
print(result)