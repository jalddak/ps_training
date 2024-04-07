def solution(begin, end):
    answer = []
    for num in range(begin, end+1):
        result = 0 if num == 1 else 1
        for i in range(2, int(num**0.5)+1):
            if num % i != 0:
                continue
            if num // i <= 10000000:
                result = num//i
                break
            else:
                result = i
        answer.append(result)
    return answer