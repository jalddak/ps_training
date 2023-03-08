from collections import deque

def solution(priorities, location):
    answer = 0
    s_ps = sorted(priorities)
    priorities = deque(priorities)
    while True:
        move = priorities.popleft()
        if location != 0:
            if move == s_ps[len(s_ps)-1]:
                s_ps.pop()
                answer += 1
            else:
                priorities.append(move)
            location -= 1
        else:
            if move == s_ps[len(s_ps)-1]:
                answer += 1
                return answer
            else:
                priorities.append(move)
                location += len(s_ps)-1