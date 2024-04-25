def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        cnt = 0
        for s in range(1, int(n ** 0.5)+1):
            if n%s != 0:
                continue
            cnt += 1
            if n/s != s:
                cnt += 1
        if cnt % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer
