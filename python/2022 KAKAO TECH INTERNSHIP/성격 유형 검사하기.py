def solution(survey, choices):
    answer = ''
    chart = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        score = abs(4-c)
        if c > 4:
            chart[s[1]] += score
        else:
            chart[s[0]] += score
    
    if chart['R'] < chart['T']:
        answer += 'T'
    else:
        answer += 'R'
        
    if chart['C'] < chart['F']:
        answer += 'F'
    else:
        answer += 'C'
        
    if chart['J'] < chart['M']:
        answer += 'M'
    else:
        answer += 'J'
        
    if chart['A'] < chart['N']:
        answer += 'N'
    else:
        answer += 'A'
        
    return answer