def solution(k, tangerine):
    answer = 0
    d = {}
    for t in tangerine:
        d[t] = d.get(t, 0) + 1
    cnts = sorted(list(d.values()), reverse=True)
    for cnt in cnts:
        k -= cnt
        answer += 1
        if k <= 0:
            break
    return answer