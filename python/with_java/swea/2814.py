tcCnt = int(input())

def recursion(edges, visited, node, depth):
    result = depth
    for next in edges[node]:
        if visited[next]:
            continue
        visited[next] = True
        result = max(result, recursion(edges, visited, next, depth+1))
        visited[next] = False
    return result

answer = []
for tc in range(1, tcCnt + 1):
    n, m = map(int, input().split())
    edges = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    for _ in range(m):
        f, s = map(int, input().split())
        edges[f].append(s)
        edges[s].append(f)

    result = 1
    for i in range(1, n+1):
        visited[i] = True
        result = max(result, recursion(edges, visited, i, 1))
        visited[i] = False
    

    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)

print("\n".join(answer))