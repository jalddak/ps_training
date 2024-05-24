def solution(dartResult):
    scores = []
    sqrt = {'S':1, 'D':2, 'T':3}
    num = ''
    for c in dartResult:
        if c.isdigit():
            num += c
            continue
        if num != '':
            scores.append(int(num))
            num = ''
        if c in sqrt:
            scores[-1] **= sqrt[c]
        if c == '*':
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2
        if c == '#':
            scores[-1] = -scores[-1]
    answer = sum(scores)
    return answer