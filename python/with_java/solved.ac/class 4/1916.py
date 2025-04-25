# 첫번째 코드
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 차이점 -> distance 형태 (리스트형태)
distance = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    distance[s].append([e, cost])

s, e = map(int, input().split())

import heapq

heap = [(0, s)]
check = [1e9 for _ in range(n+1)]
check[s] = 0

while heap:
    cost, x = heapq.heappop(heap)
    if x == e:
        print(cost)
        break
    if cost > check[x]:
        continue
    for nx, plus in distance[x]:
        nCost = cost + plus
        if check[nx] <= nCost:
            continue
        heapq.heappush(heap, (nCost, nx))
        check[nx] = nCost

# 두번째 코드
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 차이점 -> distance 형태 (딕셔너리(자바로 치면 HashMap) 형태)
distance = dict()
for _ in range(m):
    s, e, cost = map(int, input().split())
    if s not in distance:
        distance[s] = {e : cost}
    else:
        distance[s][e] = cost if e not in distance[s] or distance[s][e] > cost else distance[s][e]

s, e = map(int, input().split())

import heapq

heap = [(0, s)]
check = [1e9 for _ in range(n+1)]
check[s] = 0

while heap:
    cost, x = heapq.heappop(heap)
    if x == e:
        print(cost)
        break
    if cost > check[x] or x not in distance:
        continue
    for nx in distance[x]:
        nCost = cost + distance[x][nx]
        if check[nx] <= nCost:
            continue
        heapq.heappush(heap, (nCost, nx))
        check[nx] = nCost
