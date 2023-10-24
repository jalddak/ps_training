N, M, R = list(map(int, input().split()))

visited = [False for _ in range(N+1)]
tree = {}
for _ in range(M):
    node1, node2 = list(map(int, input().split()))
    if node1 not in tree:
        tree[node1] = [node2]
    else:
        tree[node1].append(node2)
    if node2 not in tree:
        tree[node2] = [node1]
    else:
        tree[node2].append(node1)

order = [0 for _ in range(N+1)]
n = 1
stack = [R]

while len(stack) != 0:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        order[node] = n
        n += 1
        if node in tree:
            tree[node].sort(reverse = True)
            for next in tree[node]:
                stack.append(next)

for i in range(1, len(order)):
    print(order[i])