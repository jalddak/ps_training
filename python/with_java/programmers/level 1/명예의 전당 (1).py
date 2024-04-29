import heapq

def solution(k, score):
    heap = []
    answer = []
    for s in score:
        if len(heap) < k:
            heapq.heappush(heap, s)
        elif heap[0] < s:
            heapq.heappop(heap)
            heapq.heappush(heap, s)
        answer.append(heap[0])
    return answer