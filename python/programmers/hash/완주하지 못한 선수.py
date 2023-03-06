def solution(participant, completion):
    answer = ''
    p_dict = {}
    
    for p in participant:
        if p not in p_dict:
            p_dict[p] = 1
        else:
            p_dict[p] += 1
    
    for c in completion:
        p_dict[c] -= 1
    
    for p in participant:
        if p_dict[p] != 0:
            answer = p
            break
    return answer