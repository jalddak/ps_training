def solution(k, dungeons):
    answer = []
    for index in range(len(dungeons)):
        if dungeons[index][0] <= k:
            answer.append(1)
            new_dungeons = dungeons[:]
            new_dungeons.pop(index)
            if len(new_dungeons) != 0:
                new_k = k - dungeons[index][1]
                answer[index] += solution(new_k, new_dungeons)
        else :
            answer.append(0)
    answer = max(answer)
    
    return answer