import heapq
from collections import deque

def solution(jobs):
    answer = 0

    length = len(jobs)
    jobs.sort(key = lambda x: (x[0], x[1]))
    jobs = deque(jobs)
    end = 0
    heap = []

    while len(jobs) > 0 or len(heap) > 0:
        while (len(jobs) > 0 and jobs[0][0] <= end):
            job = jobs.popleft()
            heapq.heappush(heap, (end+job[1], job[0]))
        if len(heap) == 0:
            job = jobs.popleft()
            end = job[0] + job[1]
            answer += job[1]
            continue

        new_end, start = heapq.heappop(heap)
        time = new_end - end
        answer += new_end - start
        heap = list(map(lambda x:(x[0]+time, x[1]), heap))
        end = new_end

    return answer // length