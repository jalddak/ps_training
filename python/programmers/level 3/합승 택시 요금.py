import heapq

def solution(n, s, a, b, fares):
    answer = 100000 * n + 1
    together = [0 for _ in range(n+1)]
    visited = set()
    edges = [[] for _ in range(n+1)]
    for fare in fares:
        start, end, cost = fare
        edges[start].append((end, cost))
        edges[end].append((start, cost))
    heap = [(0, s)]
    while len(visited) != n and heap:
        cost, start = heapq.heappop(heap)
        if start in visited:
            continue
        visited.add(start)
        together[start] = cost
        for edge in edges[start]:
            heapq.heappush(heap, (cost+edge[1], edge[0]))
            
    for i in range(1, n+1):
        heap = [(0, i)]
        min_costs = [0 for _ in range(n+1)]
        visited = [False for _ in range(n+1)]
        while (not visited[a] or not visited[b]) and heap:
            cost, node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            min_costs[node] = cost
            for edge in edges[node]:
                heapq.heappush(heap, (cost+edge[1], edge[0]))
        result = min_costs[a] + min_costs[b] + together[i]
        if not visited[a] or not visited[b]:
            continue
        answer = min(answer, result)
    
    return answer