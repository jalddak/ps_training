N = int(input())

from collections import deque
queue = deque([[0, [N]]])
visited = [False for _ in range(N)]

while queue:
    cnt, nums = queue.popleft()
    x = nums[-1]
    if x == 1:
        print(cnt)
        print(" ".join(map(str, nums)))
        exit()

    if x % 3 == 0 and not visited[x//3]:
        queue.append([cnt+1, nums+[x//3]])
        visited[x//3] = True
    if x % 2 == 0 and not visited[x//2]:
        queue.append([cnt+1, nums+[x//2]])
        visited[x//2] = True
    if not visited[x-1]:
        queue.append([cnt+1, nums+[x-1]])
        visited[x-1] = True


N = int(input())

from collections import deque
queue = deque([[0, N]])
dp = [[] for _ in range(N+1)]
dp[N] = [N]

while queue:
    cnt, x = queue.popleft()
    if x == 1:
        print(cnt)
        print(" ".join(map(str, dp[x])))
        exit()

    if x % 3 == 0 and len(dp[x//3]) == 0:
        queue.append([cnt+1, x//3])
        dp[x//3] = dp[x] + [x//3]
    if x % 2 == 0 and len(dp[x//2]) == 0:
        queue.append([cnt+1, x//2])
        dp[x//2] = dp[x] + [x//2]
    if len(dp[x-1]) == 0:
        queue.append([cnt+1, x-1])
        dp[x-1] = dp[x] + [x-1]