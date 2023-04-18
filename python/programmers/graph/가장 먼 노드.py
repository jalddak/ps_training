from collections import deque

def solution(n, edge):
    answer = 0
    for i in range(len(edge)):
        edge[i].sort()
    edge.sort(key = lambda x:(x[0], x[1]))
    edge = deque(edge)
    dic_num = {}
    while len(edge) != 0:
        vertex = edge.popleft()
        if vertex[0] in dic_num:
            dic_num[vertex[0]].append(vertex[1])
        else:
            dic_num[vertex[0]] = [vertex[1]]
        if vertex[1] in dic_num:
            dic_num[vertex[1]].append(vertex[0])
        else:
            dic_num[vertex[1]] = [vertex[0]]
    queue = deque([1])
    distance = {1:0}
    while len(queue) != 0:
        search = queue.popleft()
        for check in dic_num[search]:
            if check not in distance:
                distance[check] = distance[search] + 1
                queue.append(check)
    distance_array = list(distance.values())
    max_dis = max(distance_array)
    for d in distance_array:
        if max_dis == d:
            answer += 1
    return answer