# dfs

node_num = int(input())
edge_num = int(input())

nodes = [[] for _ in range(node_num)]
visited = [False for _ in range(node_num)]

for _ in range(edge_num):
    node1, node2 = list(map(lambda x: x-1, list(map(int, input().split()))))
    nodes[node1].append(node2)
    nodes[node2].append(node1)

stack = [0]

while len(stack) != 0:
    num = stack.pop()
    if not visited[num]:
        visited[num] = True
        stack += nodes[num]

print(visited.count(True)-1)