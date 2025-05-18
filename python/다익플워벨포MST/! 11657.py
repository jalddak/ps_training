import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

INF = int(1e9)
costs = [INF for _ in range(N+1)]

def check_minus_rotate(start):
    global edges, costs, N, M
    costs[start] = 0
    for i in range(N):
        for j in range(M):
            a, b, c = edges[j]
            if costs[a] != INF and costs[a] + c < costs[b]:
                costs[b] = costs[a] + c
                if i == N-1:
                    return True
    return False

if check_minus_rotate(1):
    print(-1)
    exit()

for i in range(2, N+1):
    cost = costs[i]
    if cost == INF:
        print(-1)
    else: print(cost)