def solution(array, n):
    answer = 0
    array.sort()
    for num in array:
        if abs(answer - n) > abs(num - n):
            answer = num
    return answer