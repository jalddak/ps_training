import math

def solution(r1, r2):
    answer = 0
    for i in range(r2+1):
        max_height = int((r2**2 - i**2) ** 0.5)
        min_height = math.ceil((r1**2 - i**2) ** 0.5) if r1 > i else 0
        cnt = max_height - min_height + 1
        answer += 4 * cnt
    answer -= 4 * (r2 - r1 + 1)
        
    return answer