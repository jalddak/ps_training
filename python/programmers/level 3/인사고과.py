def solution(scores):
    answer = 1
    w = scores[0]
    l_rank = sorted(scores, key=lambda x:(-x[0], x[1]))
    scores = [l_rank[0]] if l_rank else []
    for i in range(1, len(l_rank)):
        score = l_rank[i]
        if score[0] > w[0] and score[1] > w[1]:
            return -1
        if scores[-1][0] > score[0] and scores[-1][1] > score[1]:
            continue
        scores.append(score)
    scores.sort(key=lambda x:x[0]+x[1], reverse=True)
    for score in scores:
        if sum(score) <= sum(w):
            break
        answer += 1
        
    return answer