from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    edges = [[] for _ in range(n+1)]
    for s, e in roads:
        edges[s].append(e)
        edges[e].append(s)
        
    visited = [-1 for _ in range(n+1)]
    visited[destination] = 0
    queue = deque([destination])
    while queue:
        current = queue.popleft()
        for node in edges[current]:
            if visited[node] != -1:
                continue
            visited[node] = visited[current]+1
            queue.append(node)
    
    for s in sources:
        answer.append(visited[s])
        
    return answer