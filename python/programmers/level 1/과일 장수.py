def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    trash = len(score) % m
    
    for i in range(trash):
        score.pop()
    
    for i in range(len(score)):
        if (i+1) % m == 0:
            answer += m*score[i]
            
    return answer