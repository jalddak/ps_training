n, l = map(int, input().split())

nums = list(map(int, input().split()))

from collections import deque

q = deque()
answer = []
for i in range(n):
    num = nums[i]
    while q and q[0][1] < i - l + 1:
        q.popleft()
    while q and q[-1][0] >= num:
        q.pop()
    q.append([num, i])
    answer.append(q[0][0])

print(*answer)