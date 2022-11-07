def solution(my_string):
    answer = []
    for letter in my_string:
        if letter.isupper():
            answer.append(letter.lower())
        else:
            answer.append(letter.upper())
    answer = ''.join(answer)
    return answer