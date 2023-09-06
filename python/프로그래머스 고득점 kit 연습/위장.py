def solution(clothes):
    answer = 1
    cd = {}
    for name, t in clothes:
        if t not in cd:
            cd[t] = 2
        else:
            cd[t] += 1
    
    for key in cd:
        answer *= cd[key]
    answer -= 1
        
    return answer