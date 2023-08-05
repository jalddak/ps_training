# BFS
from collections import deque

K = int(input())

for _ in range(K):
    V, E = list(map(int, input().split()))
    graph = [[] for _ in range(V)]
    for _ in range(E):
        f, s = list(map(lambda x:x-1, list(map(int, input().split()))))
        graph[f].append(s)
        graph[s].append(f)
    
    colors = [0 for _ in range(V)]
    for i in range(V):
        check = True
        if colors[i] == 0:
            queue = deque([[i, graph[i]]])
            colors[i] = 1
            while len(queue) != 0:
                parent, children = queue.popleft()
                color = 0
                if colors[parent] >= 0:
                    color = -1
                else:
                    color = 1
                for child in children:
                    if colors[child] == 0:
                        colors[child] = color
                        queue.append([child, graph[child]])
                    elif colors[child] != color:
                        check = False
                        break
                if not check:
                    break
            if not check:
                    break
    if not check:
        print('NO')
    else:
        print('YES')