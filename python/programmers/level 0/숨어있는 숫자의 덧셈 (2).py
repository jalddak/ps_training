def solution(my_string):
    answer = 0
    index = 0
    num = ''
    while index < len(my_string):
        if my_string[index].isdigit():
            num += my_string[index]
        elif len(num) != 0:
            answer += int(num)
            num = ''
        index += 1
    if len(num) != 0:
        answer += int(num)
    return answer