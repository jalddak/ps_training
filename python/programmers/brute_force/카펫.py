import math

def solution(brown, yellow):
    answer = []
    candidates = []
    for n in range(1, int(math.sqrt(yellow) + 1)):
        if yellow % n == 0:
            candidates.append(n)
    for n in candidates:
        length = n
        width = yellow // n
        predict = 2 * (width + length) + 4
        if predict == brown:
            answer = [width + 2, length + 2]
            break
    return answer