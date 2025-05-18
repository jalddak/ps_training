# heap 이용해서 푸는 문제라고함. dfs로 조건 최대한 걸러가며 풀려고했는데 안됨.
# 61.3점

def dfs(node, summits, paths, gates, routes, intensity, max_cost):
    print(node, routes, intensity, max_cost)
    if node in summits:
        print(node, intensity, 'summit')
        return [node, intensity]
    result = [-1, max_cost]
    for next_node, cost in paths[node]:
        if next_node in routes or next_node in gates:
            continue
        if (result[0] == -1 or result[1] >= max(intensity, cost)) and max_cost >= cost:
            candidate = dfs(next_node, summits, paths, gates, routes+[next_node], max(intensity, cost), result[1])
            if candidate[0] != -1:
                if result[0] == -1:
                    result = candidate
                elif result[1] > candidate[1]:
                    result = candidate
                elif result[1] == candidate[1] and result[0] > candidate[0]:
                    result = candidate
        else:
            break
    print(result, node)
    return result
        

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
        paths_dict[p].sort(key = lambda x:x[1])
    
    answer = [-1, max_cost]
    for g in gates:
        candidate = dfs(g, summits, paths_dict, gates, [g], 0, answer[1])
        if candidate[0] != -1:
            if answer[0] == -1:
                answer = candidate
            elif answer[1] > candidate[1]:
                answer = candidate
            elif answer[1] == candidate[1] and answer[0] > candidate[0]:
                answer = candidate
    return answer

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
# n = 7
# paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
# gates = [2]
# summits = [3, 4]
# print(solution(n, paths, gates, summits))
# print(solution())
# print(solution())


# 58.1점
import sys
sys.setrecursionlimit(2**20)

def dfs(node_lists, summits, paths, gates, routes, intensity, max_cost):
    candidates = []
    for node in node_lists:
        for next_node, cost in paths[node]:
            candidates.append([node, next_node, cost])
    candidates.sort(key = lambda x:x[2])
    
    result = [-1, max_cost]
    for node, next_node, cost in candidates:
        if next_node in routes or next_node in gates:
            continue
        if next_node in summits and (result[0] == -1 or result[1] > max(intensity,cost) or (result[1] == max(intensity,cost)and result[0] > next_node)):
            return [next_node, max(intensity,cost)]
        if (result[0] == -1 or result[1] >= max(intensity, cost)) and max_cost >= cost:
            candidate = dfs([next_node], summits, paths, gates, routes|set([node]), max(intensity, cost), result[1])
            if candidate[0] != -1:
                if result[0] == -1:
                    result = candidate
                elif result[1] > candidate[1]:
                    result = candidate
                elif result[1] == candidate[1] and result[0] > candidate[0]:
                    result = candidate

    return result
        

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
        paths_dict[p].sort(key = lambda x:x[1])
    
    answer = dfs(gates, set(summits), paths_dict, set(gates), set([]), 0, max_cost)
    return answer


# 64.5점
import sys
sys.setrecursionlimit(2**20)
visited = []

def dfs(node_lists, summits, paths, gates, routes, intensity, max_cost):
    candidates = []
    for node in node_lists:
        for next_node, cost in paths[node]:
            candidates.append([node, next_node, cost])
    candidates.sort(key = lambda x:x[2])
    
    result = [-1, max_cost]
    for node, next_node, cost in candidates:
        if next_node in routes or next_node in gates:
            continue
        if len(visited[node]) != 0:
            return visited[node]
        candidate = []
        if next_node in summits:
            candidate = [next_node, max(intensity,cost)]
        elif (result[0] == -1 or result[1] >= max(intensity, cost)) and max_cost >= cost:
            candidate = dfs([next_node], summits, paths, gates, routes|set([node]), max(intensity, cost), result[1])
        if len(candidate) != 0 and candidate[0] != -1:
            if result[0] == -1:
                result = candidate
            elif result[1] > candidate[1]:
                result = candidate
            elif result[1] == candidate[1] and result[0] > candidate[0]:
                result = candidate
                
    for node in node_lists:
        if result[0] != -1:
            visited[node] = result
    return result
        

def solution(n, paths, gates, summits):
    global visited
    visited = [[] for _ in range(n+1)]
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
        paths_dict[p].sort(key = lambda x:x[1])
    
    answer = dfs(gates, set(summits), paths_dict, set(gates), set([]), 0, max_cost)
    return answer

n = 7
paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
gates = [2]
summits = [3, 4]
print(solution(n, paths, gates, summits))