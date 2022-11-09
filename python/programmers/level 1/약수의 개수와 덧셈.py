def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        약수 = []
        for n in range(1, int(num ** 0.5) + 1):
            if num % n == 0:
                약수.append(n)
                약수.append(num // n)
        약수 = list(set(약수))
        if len(약수) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer