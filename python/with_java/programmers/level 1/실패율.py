def solution(N, stages):
    fail = {}
    for n in range(1, N+1):
        fail[n] = 0
    for s in stages:
        if s > N:
            continue
        fail[s] += 1
    fail = list(fail.items())
    fail.sort(key=lambda x:x[0])
    
    users = len(stages)
    info = {}
    for n in range(1, N+1):
        info[n] = 0
    for s, cnt in fail:
        info[s] = cnt / users
        users -= cnt
        if users == 0:
            break
    info = list(info.items())
    info.sort(key=lambda x:(-x[1], x[0]))
    answer = list(map(lambda x:x[0], info))
    return answer