n, k = map(int, input().split())
        
result = -1
visited = [[500001, 500001] for _ in range(500001)]
visited[n][0] = 0
stack = [(n, 0)]
time = 0
while k <= 500000:
    if visited[k][time%2] <= time:
        result = time
        break
    time += 1
    k += time

    next = []
    while stack:
        x, t = stack.pop()
        nt = t + 1
        if x-1 >= 0 and visited[x-1][nt%2] > nt:
            visited[x-1][nt%2] = nt
            next.append((x-1, nt))
        if x+1 <= 500000 and visited[x+1][nt%2] > nt:
            visited[x+1][nt%2] = nt
            next.append((x+1, nt))
        if 2*x <= 500000 and visited[2*x][nt%2] > nt:
            visited[2*x][nt%2] = nt
            next.append((2*x, nt))

    stack = next

print(result)