import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        result = first + (second * 2)
        heapq.heappush(scoville, result)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    return answer