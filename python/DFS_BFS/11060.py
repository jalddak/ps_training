N = int(input())
nums = list(map(int, input().split()))
visited = [False for _ in range(N)]
visited[0] = True

from collections import deque
queue = deque([(0, 0)])
while queue:
    loca, cnt = queue.popleft()
    if loca == N-1:
        print(cnt)
        exit()
    for n in range(1, nums[loca]+1):
        next = loca+n
        if next < N and not visited[next]:
            visited[next] = True
            queue.append((next, cnt+1))
print(-1)