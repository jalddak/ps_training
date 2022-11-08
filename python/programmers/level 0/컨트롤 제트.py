def solution(s):
    list = s.split()
    answer_list = []
    for letter in list:
        if letter == 'Z':
            answer_list.pop()
        else:
            answer_list.append(int(letter))
    answer = sum(answer_list)
    return answer