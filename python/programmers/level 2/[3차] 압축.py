def solution(msg):
    answer = []
    dictionary = {}
    dict_num = 27
    
    for i in range(1,dict_num):
        dictionary[chr(i+64)] = i
        
    index = 0
    while index < len(msg):
        w = ''
        while index < len(msg):
            c = msg[index]
            if w+c in dictionary:
                w += c
                index += 1
                if index >= len(msg):
                    answer.append(dictionary[w])
            else:
                answer.append(dictionary[w])
                dictionary[w+c] = dict_num
                dict_num += 1
                break
        
    return answer