def solution(my_string):
    my_string = my_string.lower()
    answer = list(my_string)
    answer.sort()
    answer = ''.join(answer)
    return answer