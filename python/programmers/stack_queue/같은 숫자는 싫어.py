def solution(arr):
    answer = []
    before = 10
    for num in arr:
        if num != before:
            answer.append(num)
        before = num
    return answer