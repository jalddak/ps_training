def solution(weights):
    answer = 0
    
    d_weights = {}
    for w in weights:
        d_weights[w] = d_weights.get(w, 0) + 1
    weights = list(d_weights.keys())
    
    for w in weights:
        w_cnt = d_weights[w]
        answer += w_cnt * (w_cnt-1) // 2
        answer += w_cnt * d_weights.get(w/2*3, 0)
        answer += w_cnt * d_weights.get(w/2*4, 0)
        answer += w_cnt * d_weights.get(w/3*4, 0)
    
    return answer