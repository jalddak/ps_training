import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
vs = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    vs[v1].append(v2)
    vs[v2].append(v1)

answer = 0
for i in range(1, n+1):
    q = []
    if not visited[i]:
        visited[i] = True
        answer += 1
        q = [i]
        while q:
            x = q.pop()
            for v in vs[x]:
                if not visited[v]:
                    q.append(v)
                    visited[v] = True

print(answer)