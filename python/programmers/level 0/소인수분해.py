def solution(n):
    answer = []
    소인수 = 2
    while n != 1:
        if n % 소인수 == 0:
            answer.append(소인수)
            n = n // 소인수
            소인수 = 2
        else:
            소인수 += 1
    answer = sorted(list(set(answer)))
    return answer