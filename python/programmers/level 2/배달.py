import heapq

def solution(N, road, K):
    answer = 1

    info = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    
    for a, b, c in road:
        info[a].append((b, c))
        info[b].append((a, c))
    
    visited[1] = True
    heap = []
    for to, cost in info[1]:
        if cost <= K:
            heapq.heappush(heap, (cost, to))
    
    while heap:
        cost, to = heapq.heappop(heap)
        if visited[to]:
            continue
        visited[to] = True
        answer += 1
        for n_to, n_cost in info[to]:
            if visited[n_to]:
                continue
            total = cost + n_cost
            if total <= K:
                heapq.heappush(heap, (total, n_to))

    return answer