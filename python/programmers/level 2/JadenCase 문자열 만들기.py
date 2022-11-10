def solution(s):
    index = 0
    answer = ''
    for letter in s:
        if letter == ' ':
            answer += ' '
            index = 0
        elif index == 0:
            answer += letter.upper()
            index += 1
        else:
            answer += letter.lower()
            index += 1
        
    
    return answer