import heapq

tc = int(input())

answer = []

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for c in range(1, tc+1):
    result = "#" + str(c) + " " 
    n = int(input())
    board = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    heap = [(0, 0, 0)]
    while heap:
        cnt, y, x = heapq.heappop(heap)
        if (y, x) == (n-1, n-1):
            result += str(cnt)
            break
        if visited[y][x]:
            continue
        visited[y][x] = True
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                heapq.heappush(heap, (cnt + board[ny][nx], ny, nx))
    answer.append(result)
for a in answer:
    print(a)