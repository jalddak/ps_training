import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    if scoville[0] < K:
        answer = -1
    return answer