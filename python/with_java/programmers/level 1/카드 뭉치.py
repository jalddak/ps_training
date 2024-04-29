from collections import deque
def solution(cards1, cards2, goal):
    answer = "Yes"
    c1 = deque(cards1)
    c2 = deque(cards2)
    for s in goal:
        if c1 and c1[0] == s:
            c1.popleft()
            continue
        if c2 and c2[0] == s:
            c2.popleft()
            continue
        answer = "No"
        break
        
    return answer