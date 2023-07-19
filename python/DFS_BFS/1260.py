# DFS_BFS
from collections import deque


N, M, V = list(map(int, input().split()))

graph = {}

for i in range(M):
    node1, node2 = list(map(int, input().split()))
    if node1 in graph:
        graph[node1].append(node2)
    else:
        graph[node1] = [node2]
    
    if node2 in graph:
        graph[node2].append(node1)
    else:
        graph[node2] = [node1]

def DFS():
    global N, V, graph

    visited = [False for _ in range(N+1)]
    stack = [V]

    check = 0
    while check != N and len(stack) != 0:
        num = stack.pop()
        if not visited[num]:
            visited[num] = True
            if num in graph:
                graph[num].sort(reverse = True)
                stack += graph[num]
            check += 1
            print(num, end = ' ')
    print()


def BFS():
    global N, V, graph
    visited = [False for _ in range(N+1)]
    queue = deque([V])

    check = 0
    while check != N and len(queue) != 0:
        num = queue.popleft()
        if not visited[num]:
            visited[num] = True
            if num in graph:
                graph[num].sort()
                queue += graph[num]
            check += 1
            print(num, end = ' ')
    print()


if __name__ == '__main__':
    DFS()
    BFS()