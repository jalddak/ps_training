def solution(sequence, k):
    answer = []
    total = 0
    start = 0
    nl = []
    candidate = []
    for i in range(len(sequence)):
        total += sequence[i]
        while start < i and total > k:
            total -= sequence[start]
            start += 1
        if total == k:
            candidate.append([start, i])
    candidate.sort(key=lambda x:abs(x[1]-x[0]))
    answer = candidate[0]
    return answer