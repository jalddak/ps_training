def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(-x[0], -x[1]))
    while targets:
        s, e = targets.pop()
        while targets:
            ns, ne = targets[-1]
            if ns < e:
                targets.pop()
                if ne < e:
                    e = ne
            else:
                break
        answer += 1
        
    return answer