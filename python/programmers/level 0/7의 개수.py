def solution(array):
    answer = 0
    for num in array:
        for letter in str(num):
            if letter == '7':
                answer += 1
    return answer