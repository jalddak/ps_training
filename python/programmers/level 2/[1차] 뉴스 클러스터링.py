def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    list1 = []
    list2 = []
    for i in range(len(str1)-1):
        word = str1[i] + str1[i+1]
        if str1[i].islower() and str1[i+1].islower():
            list1.append(word)
    for i in range(len(str2)-1):
        word = str2[i] + str2[i+1]
        if str2[i].islower() and str2[i+1].islower():
            list2.append(word)
    
    dict1 = {}
    dict2 = {}
    교집합 = 0
    합집합 = 0
    for word in list1:
        if word not in dict1:
            dict1[word] = 1
        else:
            dict1[word] += 1
    for word in list2:
        if word not in dict2:
            dict2[word] = 1
        else:
            dict2[word] += 1
    
    for word in dict1:
        if word in dict2:
            교집합 += min(dict1[word], dict2[word])
            합집합 += max(dict1[word], dict2[word])
        else:
            합집합 += dict1[word]
            
    for word in dict2:
        if word not in dict1:
            합집합 += dict2[word]
    
    유사도 = 0
    if 합집합 == 0:
        유사도 = 1
    else:
        유사도 = 교집합 / 합집합
    
    answer = 유사도 * 65536 // 1
            
    
    return answer