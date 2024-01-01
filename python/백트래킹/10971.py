N = int(input())

W = [list(map(int, input().split())) for _ in range(N)]

import heapq
visited = [False for _ in range(N)]
visited[0] = True
heap = [(0, [0, visited])]

while heap:
    total, info = heapq.heappop(heap)
    now, visited = info

    if now == 0 and total != 0:
        print(total)
        exit()

    end_point = True
    for i in range(N):
        if W[now][i] != 0 and not visited[i]:
            n_visited = visited[:]
            n_visited[i] = True
            heapq.heappush(heap, (total + W[now][i], [i, n_visited]))
            end_point = False
        elif not visited[i]:
            end_point = False
    if end_point and W[now][0] != 0:
        heapq.heappush(heap, (total + W[now][0], [0, visited]))