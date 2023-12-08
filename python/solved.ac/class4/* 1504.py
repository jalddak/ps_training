# 힌트: 다익스트라 각 정점에서 하면 되겠구나
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
INF = int(1e9)
routes = [[] for _ in range(N)]

for _ in range(E):
    a, b, c = map(int, input().split())
    routes[a-1].append([b-1, c])
    routes[b-1].append([a-1, c])

v1, v2 = map(lambda x:x-1, map(int, input().split()))

import heapq

def dijkstra(start):
    shorts = [INF for _ in range(N)]
    shorts[start] = 0
    heap = [(0, start)]
    while len(heap) != 0:
        d, node = heapq.heappop(heap)
        if shorts[node] < d:
            continue
        for n_node, n_d in routes[node]:
            if shorts[n_node] < d + n_d:
                continue
            shorts[n_node] = d + n_d
            heapq.heappush(heap, (d + n_d, n_node))

    return shorts

o_shorts = dijkstra(0)
v1_shorts = dijkstra(v1)
v2_shorts = dijkstra(v2)

ov1v2n = o_shorts[v1] + v1_shorts[v2] + v2_shorts[N-1]
ov2v1n = o_shorts[v2] + v2_shorts[v1] + v1_shorts[N-1]

result = min(ov1v2n, ov2v1n)
print(result if result < INF else -1)

# 메모리 초과
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
INF = int(1e9)
routes = [[] for _ in range(N)]

for _ in range(E):
    a, b, c = map(int, input().split())
    routes[a-1].append([b-1, c])
    routes[b-1].append([a-1, c])

v1, v2 = map(lambda x:x-1, map(int, input().split()))

visited = [False for _ in range(N)]
visited[0] = True
stack = [0]

while len(stack) != 0:
    node = stack.pop()
    for n_node, n_d in routes[node]:
        if not visited[n_node]:
            stack.append(n_node)
            visited[n_node] = True

if not visited[0] or not visited[v1] or not visited[v2] or not visited[N-1]:
    print(-1)
    exit()

import heapq

shorts = [[INF, INF, INF, INF] for _ in range(N)]
shorts[0][0] = 0
heap = [(0, 0, 0)]

while len(heap) != 0:
    d, node, state = heapq.heappop(heap)
    if node == N-1 and state == 3:
        print(d)
        exit()
    if shorts[node][state] < d:
        continue
    if node == v1 and state not in set([1, 3]):
        state += 1
    if node == v2 and state not in set([2, 3]):
        state += 2
    for n_node, n_d in routes[node]:
        if shorts[n_node][state] >= d + n_d:
            heapq.heappush(heap, (d + n_d, n_node, state))