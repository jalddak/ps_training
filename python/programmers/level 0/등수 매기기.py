def solution(score):
    answer = []
    score_list = score
    score_sum = []
    for score in score_list:
        score_sum.append(sum(score))
    score_sum.sort(reverse = True)
    score_rank = {}
    for index in range(len(score_sum)):
        if score_sum[index] not in score_rank:
            score_rank[score_sum[index]] = index + 1
    for score in score_list:
        answer.append(score_rank[sum(score)])
    return answer