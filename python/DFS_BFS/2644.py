#DFS

n = int(input())
f, s = list(map(int, input().split()))
visited = [False for _ in range(n)]

m = int(input())
dfs = [[] for _ in range(n)]
for _ in range(m):
    p, c = list(map(int, input().split()))
    dfs[p-1].append(c)
    dfs[c-1].append(p)

stack = [[dfs[f-1], 1]]

while len(stack) != 0:
    l, cnt = stack.pop()
    for num in l:
        if num == s:
            print(cnt)
            exit()
        if not visited[num-1]:
            visited[num-1] = True
            stack.append([dfs[num-1], cnt+1])

print(-1)