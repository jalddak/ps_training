def solution(s):
    index = 0
    answer = ''
    for letter in s:
        if letter == ' ':
            answer += ' '
            index = 0
        else:
            if index % 2 == 0:
                answer += letter.upper()
            else:
                answer += letter.lower()
            index += 1
        
    return answer