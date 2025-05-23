import heapq

visited = [False for _ in range(100001)]
n, k = map(int, input().split())
visited[n] = True

heap = [(0, n)]
while heap:
    t, x = heapq.heappop(heap)
    if x == k:
        print(t)
        break
    if 2*x < 100001 and not visited[2*x]:
        visited[2*x] = True
        heapq.heappush(heap, (t, 2*x))
    if x-1 >= 0 and not visited[x-1]:
        visited[x-1] = True
        heapq.heappush(heap, (t+1, x-1))
    if x+1 < 100001 and not visited[x+1]:
        visited[x+1] = True
        heapq.heappush(heap, (t+1, x+1))