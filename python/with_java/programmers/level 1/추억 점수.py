def solution(name, yearning, photo):
    score = {}
    answer = []
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    for names in photo:
        result = 0
        for n in names:
            result += score.get(n, 0)
        answer.append(result)
    return answer