def solution(n):
    answer = 0
    check = 0
    루트값 = n ** 0.5
    if 루트값 % int(루트값) == 0:
        check += 1
    for i in range(1, int(루트값) + 1):
        if n % i == 0:
            answer += 1
    answer *= 2
    answer -= check
    return answer