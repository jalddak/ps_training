# BFS

from collections import deque

result = []

t = int(input())
for _ in range(t):
    n = int(input())
    dy, dx = list(map(int, input().split()))
    stores = {}
    for _ in range(n):
        y, x = list(map(int, input().split()))
        stores[(y, x)] = 1
    ay, ax = list(map(int, input().split()))

    queue = deque([(dy, dx)])
    hs = 0
    while len(queue) != 0:
        y, x = queue.popleft()
        if abs(y - ay) + abs(x - ax) <= 1000:
            hs = 1
            break
        for cy, cx in list(stores.keys()):
            if stores[(cy, cx)] == 1:
                if abs(y - cy) + abs(x - cx) <= 1000:
                    stores[(cy, cx)] = 0
                    queue.append((cy, cx))
    
    result.append(["sad", "happy"][hs])

for r in result:
    print(r)