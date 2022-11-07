def solution(my_string):
    answer = 0
    for letter in my_string:
        if letter.isdigit():
            answer += int(letter)
    return answer