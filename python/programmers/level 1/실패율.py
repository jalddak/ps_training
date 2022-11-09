def solution(N, stages):
    stage_info = {}
    usernum = len(stages)
    for num in range(N):
        stageusernum = stages.count(num+1)
        if usernum == 0:
            stage_info[num+1] = 0
        else:
            stage_info[num+1] = stageusernum / usernum
        usernum -= stageusernum
    
    answer = dict(sorted(stage_info.items(), key=lambda x:x[1], reverse=True))

    return list(answer.keys())