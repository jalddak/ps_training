from collections import deque

def solution(numbers, target):
    answer = 0
    candidates = deque([0])
    while len(numbers) != 0:
        cnt = len(candidates)
        num = numbers.pop()
        for _ in range(cnt):
            candidate = candidates.popleft()
            f = candidate + num
            s = candidate - num
            candidates.append(f)
            candidates.append(s)
    for c in candidates:
        if c == target:
            answer += 1
            
    return answer