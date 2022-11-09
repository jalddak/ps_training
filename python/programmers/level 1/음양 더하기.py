def solution(absolutes, signs):
    answer = 0
    length = len(signs)
    for index in range(length):
        if signs[index]:
            answer += absolutes[index]
        else:
            answer -= absolutes[index]
    return answer