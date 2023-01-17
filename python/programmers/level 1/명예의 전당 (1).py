def solution(k, score):
    answer = []
    ranks = []
    for s in score:
        if len(ranks) < k:
            ranks.append(s)
            ranks.sort(reverse=True)
        elif ranks[k-1] < s:
            ranks.pop()
            ranks.append(s)
            ranks.sort(reverse=True)
        answer.append(ranks[len(ranks)-1])
    return answer