def solution(gems):
    answer = []
    num = len(set(gems))
    info = {}
    start = 0
    end = 0
    
    
    while len(info) != num:
        info[gems[end]] = info.get(gems[end], 0) + 1
        end += 1
    end -= 1
    
    answer = [start+1, end+1]
    
    need = set()
    while end < len(gems):
        while not need and start <= end:
            if end-start < answer[1]-answer[0]:
                answer = [start+1, end+1]
            info[gems[start]] -= 1
            if info[gems[start]] == 0:
                need.add(gems[start])
                start += 1
                break
            start += 1
        end += 1
        if end == len(gems):
            break
        info[gems[end]] += 1
        if gems[end] in need:
            need.remove(gems[end])
            
    return answer