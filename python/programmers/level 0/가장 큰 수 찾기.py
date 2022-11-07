def solution(array):
    answer = [0, 0]
    for index in range(len(array)):
        if array[index] > answer[0]:
            answer[0] = array[index]
            answer[1] = index
    return answer