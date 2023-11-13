# DFS

N = int(input())
l = [int(input()) for _ in range(N)]
l = list(map(lambda x:x-1, l))
visited = [0 for _ in range(N)]

result = []
for n in range(N):
    stack = []
    i = n
    while True:
        if visited[i] == 0:
            visited[i] = 1
            stack.append(i)
            i = l[i]
        elif visited[i] == 1 and i in stack:
            result.append(i)
            stack.remove(i)
            i = l[i]
        else:
            break

result.sort()
print(len(result))
for n in result:
    print(n+1)
