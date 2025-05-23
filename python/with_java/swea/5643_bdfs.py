tcCnt = int(input())

def recursion(edges, node, visited):
    result = 0
    for next in edges[node]:
        if visited[next]:
            continue
        visited[next] = True
        result += 1
        result += recursion(edges, next, visited)
    return result


answer = []
for tc in range(1, tcCnt + 1):
    n = int(input())
    m = int(input())
    tallEdges = [[] for _ in range(n)]
    smallEdges = [[] for _ in range(n)]
    for _ in range(m):
        s, e = map(lambda x:x-1, map(int, input().split()))
        tallEdges[s].append(e)
        smallEdges[e].append(s)
    
    result = 0
    for i in range(n):
        cnt = 0
        visited = [False for _ in range(n)]
        visited[i] = True
        cnt += recursion(tallEdges, i, visited)
        visited = [False for _ in range(n)]
        visited[i] = True
        cnt += recursion(smallEdges, i, visited)
        if cnt == n - 1:
            result += 1


    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)

print("\n".join(answer))