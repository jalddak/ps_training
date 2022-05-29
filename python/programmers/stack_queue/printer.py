def solution(priorities, location):
    answer = 0
    i = 0
    while len(priorities) != 0:
        i += 1
        if len(priorities) == 1:
            answer += 1
            priorities.pop(0)
            break
        if priorities[0] < priorities[i]:
            priorities.append(priorities.pop(0))
            i = 0
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
            continue
        if i == len(priorities) - 1:
            answer += 1
            i = 0
            priorities.pop(0)
            if location == 0:
                break
            location -= 1
    return answer