tc = int(input())
INF = 10000 * 500 + 1

answer = []

def checkEdges(s, e, t, edges):
    if s not in edges:
        edges[s] = {e : t}
    elif e not in edges[s] or edges[s][e] > t:
        edges[s][e] = t

def bf(start):
    result = [INF for _ in range(n+1)]
    # result[start] = 0
    for i in range(n):
        for s in edges:
            for e in edges[s]:
                t = edges[s][e]
                if result[e] <= result[s] + t:
                    continue
                result[e] = result[s] + t
                if i == n - 1:
                    return True
    return False

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = {}
    for _ in range(m):
        s, e, t = map(int, input().split())
        checkEdges(s, e, t, edges)
        checkEdges(e, s, t, edges)
    for _ in range(w):
        s, e, t = map(int, input().split())
        checkEdges(s, e, -t, edges)

    flag = bf(1)

    if flag:
        answer.append("YES")
    else:
        answer.append("NO")

for a in answer:
    print(a)