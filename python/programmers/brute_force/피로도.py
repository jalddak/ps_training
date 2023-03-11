def solution(k, dungeons):
    answer = []
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            answer.append(1)
            new_k = k - dungeons[i][1]
            new_dungeons = dungeons[:]
            new_dungeons.pop(i)
            if len(new_dungeons) != 0:
                answer[i] += solution(new_k, new_dungeons)
        else:
            answer.append(0)
    answer = max(answer)
            
    return answer