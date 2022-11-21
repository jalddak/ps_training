def solution(number, limit, power):
    answer = 0
    for num in range(1, number+1):
        yaksu = []
        for x in range(1, int(num ** 0.5 + 1)):
            if num % x == 0:
                yaksu.append(x)
                if num // x != x:
                    yaksu.append(num // x)
        if len(yaksu) > limit:
            answer += power
        else:
            answer += len(yaksu)
            
    return answer