def solution(my_str, n):
    answer = []
    length = len(my_str)
    f_index = 0
    s_index = n
    while s_index < length:
        answer.append(my_str[f_index:s_index])
        f_index += n
        s_index += n
    answer.append(my_str[f_index:])
    return answer