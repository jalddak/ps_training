def solution(topping):
    answer = 0
    cnt = len(set(topping))
    d = {}
    for t in topping:
        d[t] = d.get(t, 0) + 1
    s = set()
    while topping and cnt >= len(s):
        t = topping.pop()
        d[t] -= 1
        if d[t] == 0:
            cnt -= 1
        s.add(t)
        if cnt == len(s):
            answer += 1
        
    return answer