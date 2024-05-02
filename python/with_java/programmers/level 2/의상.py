def solution(clothes):
    answer = 1
    d = {}
    for c in clothes:
        d[c[1]] = d.get(c[1], 0)+1
    for key in d:
        answer *= d[key]+1
    answer -= 1
    return answer