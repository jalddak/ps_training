def solution(order):
    answer = 0
    order = str(order)
    for num in order:
        if num in '369':
            answer += 1
    return answer