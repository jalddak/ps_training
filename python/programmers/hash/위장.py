def solution(clothes):
    c_dict = {}
    for c in clothes:
        if c[1] not in c_dict:
            c_dict[c[1]] = 1
        else:
            c_dict[c[1]] += 1
    
    answer = 1
    for num in list(c_dict.values()):
        answer *= (num+1)
    answer -= 1
    
    return answer