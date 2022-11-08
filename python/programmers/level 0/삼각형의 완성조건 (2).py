def solution(sides):
    answer = 0
    sides.sort()
    for num in range(1, sides[1]):
        if sides[0] + num > sides[1]:
            answer += 1
            
    for num in range(sides[1], sides[0] + sides[1]):
        answer += 1
    return answer