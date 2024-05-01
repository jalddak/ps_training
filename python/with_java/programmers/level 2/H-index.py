def solution(citations):
    citations.sort(reverse=True)
    answer = len(citations)
    for i in range(len(citations)):
        if i+1 > citations[i]:
            answer = i
            break
    return answer