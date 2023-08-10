# DFS
import sys
sys.setrecursionlimit(10000)

n = int(input())
if n == 1:
    print(0)
    exit()
    
tree = {}

for _ in range(n-1):
    p, c, edge = list(map(int, input().split()))
    if p not in tree:
        tree[p] = [[c, edge]]
    else:
        tree[p].append([c, edge])

nodes = []

def dfs(node):
    global tree, nodes
    candidate = []
    for num, edge in tree[node]:
        if num in tree:
            long = dfs(num)
            candidate.append(long + edge)
        else:
            candidate.append(edge)
    candidate.sort(reverse=True)
    candidate = candidate[:2]
    nodes.append(candidate)
    return candidate[0]

dfs(1)
result = 0
for node in nodes:
    result = max(result, sum(node))
print(result)