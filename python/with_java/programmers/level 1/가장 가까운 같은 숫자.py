def solution(s):
    answer = []
    d = {}
    for i in range(len(s)):
        c = s[i]
        if c not in d:
            answer.append(-1)
            d[c] = i
        else:
            answer.append(i-d[c])
            d[c] = i
    return answer