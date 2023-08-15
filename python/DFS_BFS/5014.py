# BFS

from collections import deque

F, S, G, U, D = list(map(int, input().split()))

queue = deque([[S, 0]])
visited = [-1 for _ in range(F+1)]
visited[S] = 0

while len(queue) != 0:
    floor, cnt = queue.popleft()
    if floor + U <= F and (visited[floor+U] == -1 or visited[floor+U] > cnt+1):
        queue.append([floor+U, cnt+1])
        visited[floor+U] = cnt+1
        
    if floor - D >= 1 and (visited[floor-D] == -1 or visited[floor-D] > cnt+1):
        queue.append([floor-D, cnt+1])
        visited[floor-D] = cnt+1

if visited[G] == -1:
    print('use the stairs')
else:
    print(visited[G])