# BFS

from collections import deque

N, K = list(map(int, input().split()))

queue = deque([[N, 0]])
locations = [100002 for _ in range(100001)]
locations[N] = 0

while len(queue) != 0:
    l, t = queue.popleft()
    if 2*l <= 100000 and locations[2*l] > t and l < K:
        queue.append([2*l, t])
        locations[2*l] = t
    if l > 0 and locations[l-1] > t+1:
        queue.append([l-1, t+1])
        locations[l-1] = t+1
    if l < 100000 and locations[l+1] > t+1:
        queue.append([l+1, t+1])
        locations[l+1] = t+1

print(locations[K])