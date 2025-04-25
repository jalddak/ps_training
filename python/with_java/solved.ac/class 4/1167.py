import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

v = int(input())

tree = {}
for _ in range(v):
    info = list(map(int, input().split()))
    n = info[0]
    tree[n] = []
    edgeInfo = info[1:-1]
    for i in range(0, len(edgeInfo), 2):
        tree[n].append([edgeInfo[i], edgeInfo[i+1]])

visited = [False for _ in range(v+1)]
result = [0 for _ in range(v+1)]

def dfs(node):
    candidates = [0]
    for child, distance in tree[node]:
        if visited[child]:
            continue
        visited[child] = True
        candidates.append(dfs(child) + distance)
        # visited[child] = False 트리라서 굳이 false 처리 안해줘도됨.
    
    candidates.sort()
    result[node] = candidates[-1] + candidates[-2] if len(candidates) >= 2 else candidates[-1]
    return candidates[-1]

visited[1] = True
dfs(1)
print(max(result))
