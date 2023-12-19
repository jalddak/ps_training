N, S = map(int, input().split())

nums = list(map(int, input().split()))

from collections import deque

queue = deque([])
temp = 0
result = N

for n in nums:
    if n >= S:
        print(1)
        exit()
    else:
        temp += n
        queue.append(n)
    while temp - queue[0] >= S:
        temp -= queue.popleft()
    if temp >= S:
        result = min(result, len(queue))

if temp >= S:
    print(result)
else:
    print(0)