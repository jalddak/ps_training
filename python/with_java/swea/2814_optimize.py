tcCnt = int(input())

def recursion(edges, visited, node, depth):
    result = [depth, node]
    for next in edges[node]:
        if visited[next]:
            continue
        visited[next] = True
        temp = recursion(edges, visited, next, depth+1)
        if result[0] < temp[0]:
            result = temp
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

    visited[1] = True
    temp = recursion(edges, visited, 1, 1)
    visited[1] = False
    visited[temp[1]] = True
    result = recursion(edges, visited, temp[1], 1)
    

    sb = "#" + str(tc) + " " + str(result[0])
    answer.append(sb)

print("\n".join(answer))