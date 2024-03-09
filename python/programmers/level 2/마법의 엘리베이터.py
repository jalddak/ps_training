from collections import deque

def solution(storey):
    answer = 100000000
    queue = deque([[storey, 0]])
    while queue:
        num, current = queue.popleft()
        if current > answer:
            continue
        if num == 0:
            answer = min(answer, current)
            continue
        a, b = num // 10, num % 10
        queue.append([a, current + b])
        queue.append([a+1, current + 10-b])
    
    return answer