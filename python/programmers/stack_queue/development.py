import math

def solution(progresses, speeds):
    answer = []
    end = []
    i = 0
    for progress in progresses:
        end.append(math.ceil((100 - progresses[i]) / speeds[i]))
        i += 1
    max = 0
    for day in end:
        if day > max:
            max = day
            answer.append(1)
        elif day <= max:
            answer[len(answer)-1] += 1
    return answer