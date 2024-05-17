import heapq

def solution(n, works):
    works = list(map(lambda x:-x, works))
    heapq.heapify(works)
    for _ in range(n):
        if not works:
            break
        w = heapq.heappop(works)
        w += 1
        if w == 0:
            continue
        heapq.heappush(works, w)
    answer = 0
    for w in works:
        answer += w ** 2
    return answer