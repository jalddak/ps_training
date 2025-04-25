import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
edges = [[] for _ in range(n+1)]
answer = [0 for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, input().split())
    edges[p].append([c, w])

def dfs(node):
    candidates = [0]
    for child, weight in edges[node]:
        if not edges[child]:
            candidates.append(weight)
            continue
        candidates.append(weight + dfs(child))

    candidates.sort()
    answer[node] = candidates[-1] + candidates[-2] if len(candidates) >= 2 else candidates[-1]
    return candidates[-1]

dfs(1)
print(max(answer))
