from collections import deque

def solution(n, edge):
    answer = 0
    edge.sort(key = lambda x:(x[0],x[1]))
    vertex = [[] for _ in range(n+1)]
    for e in edge:
        vertex[e[0]].append(e[1])
        vertex[e[1]].append(e[0])
    
    queue = deque([1])
    distance = {1:0}
    
    while len(queue) != 0:
        search = queue.popleft()
        for next in vertex[search]:
            if next not in distance:
                distance[next] = distance[search] + 1
                queue.append(next)
    distance_values = list(distance.values())
    distance_max = max(distance_values)
    for dv in distance_values:
        if dv == distance_max:
            answer += 1
    return answer

# from collections import deque

# def solution(n, edge):
#     answer = 0
#     graph = [[0 for _ in range(n)] for _ in range(n)]
#     for vertex in edge:
#         graph[vertex[0]-1][vertex[1]-1] = 1
#         graph[vertex[1]-1][vertex[0]-1] = 1
#     already = deque([0])
#     search_list = deque([[0]])
#     i = 0
#     while i < len(search_list):
#         k = 0
#         search = deque()
#         while k < len(search_list[i]):
#             for j in range(len(graph[search_list[i][k]])):
#                 if graph[search_list[i][k]][j] == 1:
#                     if j not in already:
#                         search.append(j)
#                         already.append(j)
#             k += 1
#         if len(search) != 0:
#             search_list.append(search)
#         if len(already) == n:
#             break
#         i += 1
#     answer = len(search_list.pop())
#     return answer


# BFS 방법 - 시간 초과
# def solution(n, edge):
#     answer = 0
#     node_list = [1]
#     answer_list = make_tree(node_list, edge)
#     answer = len(list(set(answer_list)))
#     return answer

# def make_tree(node_list, edge):
#     next_node_list = []
#     for node in node_list:
#         i = 0
#         while i < len(edge):
#             if node in edge[i]:
#                 next_node = edge.pop(i)
#                 next_node.remove(node)
#                 if next_node[0] in node_list:
#                     continue
#                 else:
#                     next_node_list.append(next_node.pop())
#                 i -= 1
#             i += 1
#     if len(next_node_list) == 0:
#         answer_list = node_list
#         return answer_list
#     answer_list = make_tree(next_node_list, edge)
#     return answer_list
        
            
solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])