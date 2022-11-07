def solution(my_string, num1, num2):
    my_string = list(my_string)
    first = my_string[num1]
    second = my_string[num2]
    my_string.pop(num1)
    my_string.insert(num1, second)
    my_string.pop(num2)
    my_string.insert(num2, first)
    answer = ''.join(my_string)
    return answer