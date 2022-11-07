def solution(rsp):
    r = '0'
    s = '2'
    p = '5'
    answer = ''
    for i in rsp:
        if i == r: 
            answer += p
        elif i == s:
            answer += r
        else:
            answer += s
    return answer