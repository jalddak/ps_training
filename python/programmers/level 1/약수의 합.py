def solution(n):
    약수 = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            약수.append(i)
            약수.append(n // i)
    약수 = list(set(약수))
    answer = sum(약수)
    return answer