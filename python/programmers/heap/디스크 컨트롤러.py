from collections import deque

def solution(jobs):
    num_jobs = len(jobs)
    answer = 0
    jobs.sort(key=lambda x: (x[0], x[1]))
    jobs = deque(jobs)
    time = 0
    queue = []
    while len(jobs) != 0 or len(queue) != 0:
        if len(queue) == 0:
            work = jobs.popleft()
            time = work[0] + work[1]
        else:
            work = queue.pop()
            time += work[1]
        while len(jobs) != 0 and time > jobs[0][0]:
            queue.append(jobs.popleft())
            
        queue.sort(key=lambda x: (x[1]), reverse = True)
        answer += time - work[0]
    
    answer = answer // num_jobs
    return answer