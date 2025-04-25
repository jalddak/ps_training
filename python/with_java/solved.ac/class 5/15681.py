import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, r, q = map(int, input().split())

nodes = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)

nodeCnt = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited[r] = True

def checkTree(node):
    cnt = 1
    for nextNode in nodes[node]:
        if visited[nextNode]:
            continue
        visited[nextNode] = True
        cnt += checkTree(nextNode)
    nodeCnt[node] = cnt
    return cnt

checkTree(r)

result = []
for _ in range(q):
    result.append(nodeCnt[int(input())])

print("\n".join(map(str, result)))