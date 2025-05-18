# 벨만 포드 알고리즘

import sys
input = sys.stdin.readline

TC = int(input())
INF = int(1e9)

def bellman_ford(start):
    min_times = [INF for _ in range(N+1)]
    min_times[start] = 0
    for i in range(N):
        for s in d:
            for e in d[s]:
                t = d[s][e]
                if min_times[e] > min_times[s] + t:
                    min_times[e] = min_times[s] + t
                    if i == N - 1:
                        return True
    return False

def make_tree(s, e, t):
    if s not in d:
        d[s] = {e : t}
    elif e not in d[s]:
        d[s][e] = t
    else:
        d[s][e] = min(d[s][e], t)


result = []
for _ in range(TC):
    N, M, W = map(int, input().split())
    d = {}
    for _ in range(M):
        S, E, T = (map(int, input().split()))
        make_tree(S, E, T)
        make_tree(E, S, T)
    for _ in range(W):
        S, E, T = (map(int, input().split()))
        make_tree(S, E, -T)

    if bellman_ford(1):
        result.append("YES")
    else:
        result.append("NO")

for r in result:
    print(r)