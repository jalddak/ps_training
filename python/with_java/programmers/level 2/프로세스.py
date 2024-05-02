from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    temp = deque([])
    for i in range(len(priorities)):
        temp.append((priorities[i], i))
    maxP = max(priorities)
    answer = 0
    while priorities:
        if priorities[0] < maxP:
            priorities.append(priorities.popleft())
            temp.append(temp.popleft())
        else:
            priorities.popleft()
            p, i = temp.popleft()
            answer += 1
            if i == location:
                break
            maxP = max(priorities)
    return answer