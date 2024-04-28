from itertools import combinations

def solution(number):
    answer = 0
    candidate = map(sum, list(combinations(number, 3)))
    for c in candidate:
        if c == 0:
            answer += 1
    
    return answer