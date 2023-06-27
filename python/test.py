import heapq

def solution(n, paths, gates, summits):
    paths_dict = {}
    max_cost = 0
    for p in paths:
        node1, node2, cost = p
        max_cost = max(max_cost, cost)
        if node1 not in paths_dict:
            paths_dict[node1] = [[node2, cost]]
        else:
            paths_dict[node1].append([node2, cost])
        if node2 not in paths_dict:
            paths_dict[node2] = [[node1, cost]]
        else:
            paths_dict[node2].append([node1, cost])
            
    for p in paths_dict:
        paths_dict[p].sort(key = lambda x:x[0])
    
    answer = [-1, max_cost]
    heap = [(0, g) for g in gates]
    heapq.heapify(heap)
    visited = [False for _ in range(n+1)]
    intensities = [10000001 for _ in range(n+1)]
    gates, summits = set(gates), set(summits)
    
    while len(heap) != 0:
        print(heap)
        cost, node = heapq.heappop(heap)
        if not visited[node]:
            intensities[node] = cost
        else:
            if answer[0] != -1:
                if intensities[node] > answer[1] or cost > answer[1] or node > answer[0]:
                    continue 
        visited[node] = True

        if node in summits:
            if answer[0] == -1 or answer[1] > intensities[node]:
                answer = [node, intensities[node]]
            elif answer[1] == intensities[node] and answer[0] > node:
                answer = [node, intensities[node]]
            continue

        for n_node, n_cost in paths_dict[node]:
            if visited[n_node] or n_node in gates:
                continue
            heapq.heappush(heap, (max(intensities[node], n_cost), n_node))
        
    return answer

n = 7
paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
gates = [2]
summits = [3, 4]
print(solution(n, paths, gates, summits))


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
# print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))