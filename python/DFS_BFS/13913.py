# BFS

from collections import deque

N, K = list(map(int, input().split()))
visited = [[-1, -1] for _ in range(200001)]

queue = deque([[N, 0]])
visited[N] = [0, -1]

min_t = -1
while len(queue) != 0:
    l, t = queue.popleft()

    t += 1
    if l > 0:
        l1 = l - 1
        if visited[l1][0] == -1:
            queue.append([l1, t])
            visited[l1][0] = t
            visited[l1][1] = l

    if l < K:
        l2 = l + 1
        if visited[l2][0] == -1:
            queue.append([l2, t])
            visited[l2][0] = t
            visited[l2][1] = l

        l3 = 2 * l
        if visited[l3][0] == -1:
            queue.append([l3, t])
            visited[l3][0] = t
            visited[l3][1] = l

    if visited[K][0] != -1:
        print(visited[K][0])
        tmp = [K]
        i = K
        for _ in range(visited[K][0]):
            i = visited[i][1]
            tmp.append(i)
        for n in reversed(tmp):
            print(n, end = ' ')
        print()

        break