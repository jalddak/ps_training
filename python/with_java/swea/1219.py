tcCnt = 10

answer = []

for _ in range(1, tcCnt + 1):
    tc, length = map(int, input().split())
    sb = "#" + str(tc) + " "

    edgeInfo = list(map(int, input().split()))

    edges = [[] for _ in range(100)]

    for i in range(0, len(edgeInfo)-1, 2):
        s, e = edgeInfo[i], edgeInfo[i+1]
        edges[s].append(e)
    
    stack = [0]
    visited = [False for _ in range(100)]
    visited[0] = True
    
    result = 0
    while stack:
        x = stack.pop()

        if x == 99:
            result = 1
            break

        for nx in edges[x]:
            if visited[nx]:
                continue
            stack.append(nx)
            visited[nx] = True

    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)