def solution(balls, share):
    answer = 1
    분모 = 1
    for i in range(share):
        answer *= balls - i
        분모 *= (i+1)
    answer = answer / 분모
    return answer