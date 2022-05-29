from collections import deque

brown = 10
yellow = 2

def solution(brown, yellow):
    answer = []
    divisor = []
    area = brown + yellow
    for i in range(1,area+1):
        if area % i == 0:
            divisor.append(i)
    divisor = deque(divisor)
    while len(divisor) != 0:
        width = 0
        length = 0
        if len(divisor) == 1:
            width = divisor.pop()
            length = width
        else:
            width = divisor.pop()
            length = divisor.popleft()
        if (width-2) * (length-2) == yellow:
            answer.append(width)
            answer.append(length)
            break

    return answer
    
solution(brown, yellow)