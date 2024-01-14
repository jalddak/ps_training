import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False for _ in range(N+1)]
bridge = [[] for _ in range(N+1)]

min_w = 0
max_w = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    bridge[a].append([b, c])
    bridge[b].append([a, c])
    max_w = max(max_w, c)

s, e = map(int, input().split())

from collections import deque
def bfs(weight):
    global N, bridge, s, e
    visited = [False for _ in range(N+1)]
    visited[s] = True

    queue = deque([s])
    while queue:
        node = queue.popleft()
        for next, able in bridge[node]:
            if not visited[next] and able >= weight:
                visited[next] = True
                queue.append(next)
                if next == e:
                    return True
    return visited[e]

answer = min_w
while min_w <= max_w:
    mid = (min_w + max_w) // 2
    if bfs(mid):
        min_w = mid + 1
        answer = mid
    else:
        max_w = mid - 1

print(answer)