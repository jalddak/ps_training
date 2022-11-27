def solution(k, tangerine):
    answer = 0
    dic = {}
    for size in tangerine:
        if size not in dic:
            dic[size] = 1
        else:
            dic[size] += 1
    dic = dict(sorted(dic.items(), key=lambda x:-x[1]))
    for key in dic:
        k -= dic[key]
        answer += 1
        if k <= 0:
            break
            
    return answer