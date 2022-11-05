def solution(survey, choices):
    indicators = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    orders = [['R','T'], ['C','F'], ['J','M'], ['A', 'N']]
    for index in range(len(survey)):
        score = choices[index] - 4
        if score > 0:
            indicators[survey[index][-1]] += score
        elif score < 0:
            indicators[survey[index][0]] -= score
    
    answer = ''
    for order in orders:
        if indicators[order[0]] >= indicators[order[1]]:
            answer += order[0]
        else:
            answer += order[1]
    return answer