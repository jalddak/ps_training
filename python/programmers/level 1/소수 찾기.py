def solution(n):
    result = []
    for num in range(2, n+1):
        for c in range(2, int(num ** 0.5) + 1):
            if num % c == 0:
                result.append(num)
                break
    answer = n-1 - len(result)
    return answer