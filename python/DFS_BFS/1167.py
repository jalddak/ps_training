# DFS
V = int(input())

tree = {}

for _ in range(V):
    edge_info = list(map(int, input().split()))
    v = edge_info[0]
    for i in range(1, len(edge_info), 2):
        if edge_info[i] == -1:
            break
        if v not in tree:
            tree[v] = [[edge_info[i], edge_info[i+1]]]
        else:
            tree[v].append([edge_info[i], edge_info[i+1]])


""" 이 코드로 해서 게속 시간초과났음. 문제는 이 코드였음.
for _ in range(V):
    edge_info = list(map(int, input().split()))
    v = edge_info[0]
    edge_info = edge_info[1:]
    while True:
        if edge_info[0] == -1:
            break
        if v not in tree:
            tree[v] = [[edge_info[0], edge_info[1]]]
        else:
            tree[v].append([edge_info[0], edge_info[1]])
        edge_info = edge_info[2:]
"""

# DFS 두번 이용한 방법
max_len = [1, 0]
visited = [False for _ in range(V+1)]
stack = [[1, 0]]
visited[1] = True

while len(stack) != 0:
    node, length = stack.pop()
    if max_len[1] < length:
        max_len = [node, length]
    for v, edge in tree[node]:
        if not visited[v]:
            stack.append([v, length+edge])
            visited[v] = True

visited = [False for _ in range(V+1)]
stack = [[max_len[0], 0]]
visited[max_len[0]] = True

while len(stack) != 0:
    node, length = stack.pop()
    if max_len[1] < length:
        max_len = [node, length]
    for v, edge in tree[node]:
        if not visited[v]:
            stack.append([v, length+edge])
            visited[v] = True

print(max_len[1])

""" 내가 처음 생각한 방법 << 이것도 됨. 문제는 위에 tree 만드는 과정이 문제였었음.
max_len = []
visited = [False for _ in range(V+1)]

def dfs(node):
    global tree, max_len, visited
    visited[node] = True
    candidate = []
    for num, edge in tree[node]:
        if not visited[num]:
            if num in tree:
                long = dfs(num)
                candidate.append(long + edge)
            else:
                candidate.append(edge)
            candidate.sort(reverse=True)
            candidate = candidate[:2]
    if len(candidate) == 0:
        return 0
    max_len.append(sum(candidate))
    return candidate[0]

dfs(1)
result = max(max_len)
print(result)
"""