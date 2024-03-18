import heapq

def solution(n, k, enemy):
    heap = []
    for i in range(len(enemy)):
        if len(heap) < k:
            heapq.heappush(heap, enemy[i])
            continue
        if heap[0] < enemy[i]:
            n -= heapq.heappop(heap)
            heapq.heappush(heap, enemy[i])
        else:
            n -= enemy[i]
        if n < 0:
            return i
    return len(enemy)