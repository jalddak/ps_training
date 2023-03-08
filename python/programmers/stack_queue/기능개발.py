import math

def solution(progresses, speeds):
    answer = []
    needs = []
    for i in range(len(progresses)):
        progress = 100 - progresses[i]
        need = math.ceil(progress/speeds[i])
        needs.append(need)
    
    complete = 0
    most = 0
    for i in range(len(needs)):
        if complete == 0:
            complete += 1
            most = needs[i]
        elif needs[i] <= most:
            complete += 1
        else:
            answer.append(complete)
            complete = 1
            most = needs[i]
        if i == len(needs) - 1:
            answer.append(complete)
    return answer