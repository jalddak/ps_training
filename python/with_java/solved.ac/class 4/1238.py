n, m, x = map(int, input().split())
edges = {}
reverseEdges = {}

def checkEdges(s, e, t, edges):
    if s not in edges:
        edges[s] = {e : t}
    elif e not in edges[s] or edges[s][e] > t:
        edges[s][e] = t

for _ in range(m):
    s, e, t = map(int, input().split())
    checkEdges(s, e, t, edges)
    checkEdges(e, s, t, reverseEdges)

import heapq

def checkMinTime(x, edges):
    heap = [(0, x)]
    result = [1000 * 100 + 1 for _ in range(n + 1)]
    result[x] = 0

    while heap:
        time, l = heapq.heappop(heap)
        if result[l] < time:
            continue
        for nl in edges[l]:
            nTime = time + edges[l][nl]
            if result[nl] <= nTime:
                continue
            result[nl] = nTime
            heapq.heappush(heap, (nTime, nl))
    return result

result1 = checkMinTime(x, edges)
result2 = checkMinTime(x, reverseEdges)
result = [result1[i] + result2[i] for i in range(1, n+1)]

print(max(result))
