def solution(s):
    answer = []
    dic = {}
    i = 0
    for letter in s:
        if letter in dic:
            answer.append(i-dic[letter])
        else:
            answer.append(-1)
        dic[letter] = i
        i += 1
        
    return answer