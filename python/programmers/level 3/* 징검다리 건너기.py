import heapq

def solution(stones, k):
    answer = 0
    
    heap = []
    for i in range(k):
        heapq.heappush(heap, (-stones[i], i))
    answer = -heap[0][0]
    
    for i in range(len(stones)-k):
        heapq.heappush(heap, (-stones[i+k], i+k))
        while heap[0][1] <= i:
            heapq.heappop(heap)
        answer = min(answer, -heap[0][0])
        
    
    return answer