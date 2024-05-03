def solution(n):
    checked = [False for _ in range(n+1)]
    answer = 0
    for num in range(2, n+1):
        if checked[num]:
            continue
        answer += 1
        for multi in range(num, n+1, num):
            checked[multi] = True
    return answer