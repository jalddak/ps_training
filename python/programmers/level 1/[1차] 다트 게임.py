def solution(dartResult):
    scores = []
    index = 0
    while index < len(dartResult):
        if dartResult[index].isdigit():
            if dartResult[index+1].isdigit():
                scores.append(int(dartResult[index:index+2]))
                index += 1
            else:
                scores.append(int(dartResult[index:index+1]))
        elif dartResult[index] == 'S':
            scores[-1] = scores[-1] ** 1
        elif dartResult[index] == 'D':
            scores[-1] = scores[-1] ** 2
        elif dartResult[index] == 'T':
            scores[-1] = scores[-1] ** 3
        elif dartResult[index] == '*':
            scores[-1] = scores[-1] * 2
            if len(scores) > 1:
                scores[-2] = scores[-2] * 2
        elif dartResult[index] == '#':
            scores[-1] = -scores[-1]
        
        index += 1
    print(scores)
    answer = sum(scores)
    return answer