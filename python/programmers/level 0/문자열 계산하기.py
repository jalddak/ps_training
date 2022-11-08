def solution(my_string):
    answer = 0
    ml = my_string.split()
    answer = int(ml[0])
    
    i = 1
    while i < len(ml):
        if ml[i] == '+':
            answer += int(ml[i+1])
        else:
            answer -= int(ml[i+1])
        i += 2
    return answer