def solution(arr, divisor):
    answer = []
    for n in arr:
        if n%divisor == 0:
            answer.append(n)
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer