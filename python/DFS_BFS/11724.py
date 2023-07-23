# DFS - pypy3 에서만 통과함
N, M = list(map(int, input().split()))

nodes = [[] for i in range(N)]
for _ in range(M):
    edge = list(map(lambda x: x-1, list(map(int, input().split()))))
    nodes[edge[0]].append(edge[1])
    nodes[edge[1]].append(edge[0])

visited = [False for _ in range(N)]
stack = []
result = 0

for i in range(N):
    if not visited[i]:
        visited[i] = True
        stack.append(i)
        result += 1
    while len(stack) != 0:
        node = stack.pop()
        for n in nodes[node]:
            if not visited[n]:
                visited[n] = True
                stack.append(n)

print(result)

# # union find (틀림, dfs로 맞아서 대충생각함, 나중에 심심하면 품)
# N, M = list(map(int, input().split()))

# uf = [i for i in range(N)]

# for _ in range(M):
#     edge = list(map(lambda x: x-1, list(map(int, input().split()))))
#     if edge[0] != uf[edge[0]] and edge[1] != uf[edge[1]]:
#         root = edge[0]
#         while root != uf[root]:
#             root = uf[root]
#         uf[root] = edge[1]
#     elif edge[0] != uf[edge[0]]:
#         uf[edge[1]] = edge[0]
#     elif edge[1] != uf[edge[1]]:
#         uf[edge[0]] = edge[1]

# result = 0
# for i in range(N):
#     if uf[i] == i:
#         result += 1

# print(result)


# 시간 초과
# N, M = list(map(int, input().split()))

# graphs = []
# for _ in range(M):
#     edge = list(map(int, input().split()))
#     node1, node2 = edge
#     check = []
#     for i in range(len(graphs)):
#         if node1 in graphs[i]:
#             check.append(i)
#         if node2 in graphs[i]:
#             check.append(i)
    
#     check = list(set(check))
#     if len(check) == 0:
#         graphs.append(edge)
#     elif len(check) == 1:
#         graphs[i] = list(set(graphs[i]+edge))
#     elif len(check) == 2:
#         graphs[check[0]] = list(set(graphs[check[0]] + graphs[check[1]]))
#         graphs.pop(check[1])

# for g in graphs:
#     N -= len(g)

# print(len(graphs) + N)