import sys
input = sys.stdin.readline
import heapq

n, e = map(int, input().split())
board = [[1001 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(e):
    start, end, cost = map(int, input().split())
    if board[start][end] <= cost:
        continue
    board[start][end] = cost
    board[end][start] = cost

m1, m2 = map(int, input().split())

def dijkstra(s, e):
    checked = [1000 * 800 + 1 for _ in range(n+1)]
    checked[s] = 0
    heap = [(0, s)]
    
    while heap:
        cost, x = heapq.heappop(heap)
        if x == e:
            return cost
        if cost > checked[x]:
            continue
        for nx in range(1, n+1):
            nCost = cost + board[x][nx]
            if nx == x or board[x][nx] == 1001 or nCost >= checked[nx]:
                continue
            heapq.heappush(heap, (nCost, nx))
            checked[nx] = nCost
    
    return -1

def solution(middle1, middle2):
    r1 = dijkstra(1, middle1)
    r2 = dijkstra(middle1, middle2)
    r3 = dijkstra(middle2, n)
    return -1 if -1 in [r1, r2, r3] else r1 + r2 + r3

result1 = solution(m1, m2)
result2 = solution(m2, m1)

answer = -1
if result1 == -1 and result2 != -1:
    answer = result2
elif result1 != -1 and result2 == -1:
    answer = result1
elif result1 != -1 and result2 != -1:
    answer = min(result1, result2)

print(answer)