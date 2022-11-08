def solution(num, total):
    answer = []
    n = total // num
    answer.append(n)
    if num % 2 != 0:
        for i in range(1, num // 2 + 1):
            answer.append(n-i)
        for i in range(1, num // 2 + 1):
            answer.append(n+i)
    else:
        answer.append(n+1)
        for i in range(1, num // 2):
            answer.append(n-i)
        for i in range(1, num // 2):
            answer.append(n+1+i)
    answer.sort()
    return answer