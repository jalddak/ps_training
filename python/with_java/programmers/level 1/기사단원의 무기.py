def solution(number, limit, power):
    answer = 0
    for num in range(1, number+1):
        cnt = 0
        for n in range(1, int(num ** 0.5)+1):
            if num % n != 0:
                continue
            if num // n != n:
                cnt += 1
            cnt += 1
        if cnt > limit:
            cnt = power
        answer += cnt
        
    return answer