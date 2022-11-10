from collections import deque

def solution(n):
    answer = 0
    candidates = deque([])
    for num in range(1, n+1):
        candidates.append(num)
        while sum(candidates) > n:
            candidates.popleft()
        if sum(candidates) == n:
            answer += 1
    return answer