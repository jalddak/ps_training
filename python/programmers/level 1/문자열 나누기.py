def solution(s):
    answer = 0
    words = []
    index = 0
    first = ''
    f_num = 0
    other = 0
    for l in s:
        if len(first) == 0:
            first = l
            f_num += 1
        elif l == first:
            f_num += 1
        else:
            other += 1
            if other == f_num:
                words.append(s[index:index+other+f_num])
                other = 0
                f_num = 0
                first = ''
        index += 1
    answer = len(words)
    
    if len(first) != 0:
        answer += 1
    
            
        
    return answer