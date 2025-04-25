n, k = map(int, input().split())
checked = [[100001, 0] for _ in range(100001)]
checked[n] = [0, 1]
import heapq

heap = [(0, n)]
while heap:
    t, x = heapq.heappop(heap)
    if checked[x][0] < t:
        continue
    
    move = [x - 1, x + 1, 2 * x]
    nt = t + 1
    for nx in move:
        if nx > 100000 or nx < 0 or checked[nx][0] < nt or (nx > k and checked[k][0] < nt + nx - k):
            continue
        if checked[nx][0] == nt:
            checked[nx][1] += 1
        else:
            checked[nx] = [nt, 1]
        heapq.heappush(heap, (nt, nx)) 

print(checked[k][0])  
print(checked[k][1])