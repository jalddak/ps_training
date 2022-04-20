from collections import deque

def solution(jobs):
    num_jobs = len(jobs)
    answer = 0
    time = 0
    jobs.sort(key=lambda x: (x[0], x[1]))
    jobs = deque(jobs)
    queue = []
    while len(jobs) != 0 or len(queue) != 0:
        if len(queue) == 0:
            work = jobs.popleft()
            time += work[0] - time + work[1]
        else:
            work = queue.pop()
            time += work[1]
        if len(jobs) != 0:
            after_work = jobs[0][0]
            while after_work < time:
                queue.append(jobs.popleft())
                if len(jobs) != 0:
                    after_work = jobs[0][0]
                else:
                    break
        queue.sort(key=lambda x: (-x[1], -x[0]))
        answer += work[1] + (time - work[1] - work[0])
        print(time)

    answer = answer//num_jobs
    print(answer)
    return answer