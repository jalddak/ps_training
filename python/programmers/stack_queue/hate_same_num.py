def solution(arr):
    answer = []
    before_num = 0
    for index in range(len(arr)):
        if index == 0 or arr[index] != before_num:
            answer.append(arr[index])
        before_num = arr[index]
    return answer