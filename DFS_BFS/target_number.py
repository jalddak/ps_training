from collections import deque

def solution(numbers, target):
    answer = 0
    numbers = deque(numbers)
    target_candidates = deque([0])
    while len(numbers) != 0:
        number = numbers.popleft()
        for _ in range(len(target_candidates)):
            target_candidate = target_candidates.popleft()
            target_candidates.append(target_candidate + number)
            target_candidates.append(target_candidate - number)
    for target_candidate in target_candidates:
        if target == target_candidate:
            answer += 1
            
    return answer