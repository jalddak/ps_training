def solution(s):
    s_list = s[2:-2].split('},{')
    l_list = []
    for s in s_list:
        num_list = [int(num) for num in s.split(',')]
        l_list.append(num_list)
        
    l_list.sort(key=lambda x:len(x))
    
    answer = []
    for l in l_list:
        num = list(set(l) - set(answer))
        answer.append(num[0])
        
    return answer