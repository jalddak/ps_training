import sys
from collections import deque

input = sys.stdin.readline

H, K, R = map(int, input().split())

leafs = [deque(map(int, input().split())) for _ in range(2**H)]
nodes = [[[deque(), deque()] for _ in range(2**h)] for h in range(H)]

day = 0

result = 0
while day < R:
    day += 1
    for h in range(H):
        for i in range(2**h):
            num = -1
            if day % 2 == 1 and nodes[h][i][0]:
                num = nodes[h][i][0].popleft()
            elif day % 2 == 0 and nodes[h][i][1]:
                num = nodes[h][i][1].popleft()
            if num == -1:
                continue
            if h == 0:
                result += num
                continue
            nodes[h-1][i//2][i%2].append(num)
    if day <= K:
        for i in range(2**H):
            nodes[-1][i//2][i%2].append(leafs[i].popleft())

print(result)
            
        
    